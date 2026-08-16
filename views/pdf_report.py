import streamlit as st
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt
import io
import tempfile
from translations import t

class PDFReport(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(0, 10, "WealthSpark V101 - Executive Financial Report", 0, 1, "C")
        self.set_font("helvetica", "I", 10)
        self.cell(0, 6, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | User: {st.session_state.current_user}", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def render(db, lang):
    st.markdown(f"<h1>📄 {t('pdf_report', lang)}</h1>", unsafe_allow_html=True)
    st.markdown("Generate and download a professional PDF report summarizing your complete financial portfolio with embedded visual charts." if lang=="English" else "Genere y descargue un informe PDF profesional que resume su cartera financiera completa con gráficos visuales.")

    accounts = db["accounts"]
    custom_assets = db["custom_assets"]
    custom_debts = db["custom_debts"]

    total_cash = sum(acc["balance"] for acc in accounts if acc["type"] in ["Cash", "Checking", "Savings"])
    total_assets = sum(acc["balance"] for acc in accounts if acc["balance"] > 0) + sum(i["value"] for i in custom_assets)
    total_liab = sum(abs(acc["balance"]) for acc in accounts if acc["balance"] < 0 or acc["type"] in ["Credit Card", "Liability"]) + sum(i["balance"] for i in custom_debts)
    net_worth = total_assets - total_liab

    if st.button(t("generate_pdf", lang)):
        try:
            # Generate Matplotlib Net Worth Chart
            fig, ax = plt.subplots(figsize=(6, 2.5))
            categories = ['Total Assets', 'Total Liabilities', 'Net Worth']
            values = [total_assets, total_liab, net_worth]
            colors = ['#10b981', '#ef4444', '#3b82f6']
            ax.bar(categories, values, color=colors)
            ax.set_ylabel('USD ($)')
            ax.set_title('Portfolio Overview Breakdown')
            plt.tight_layout()

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png', dpi=150)
            img_buf.seek(0)
            plt.close(fig)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(img_buf.getvalue())
                tmp_path = tmp.name

            pdf = PDFReport()
            pdf.add_page()
            pdf.set_font("helvetica", "", 11)

            pdf.set_font("helvetica", "B", 13)
            pdf.cell(0, 8, "1. Executive Summary", 0, 1)
            pdf.set_font("helvetica", "", 11)
            pdf.cell(0, 6, f"Net Worth: ${net_worth:,.2f}", 0, 1)
            pdf.cell(0, 6, f"Total Assets: ${total_assets:,.2f}", 0, 1)
            pdf.cell(0, 6, f"Total Liabilities: ${total_liab:,.2f}", 0, 1)
            pdf.cell(0, 6, f"Total Cash Reserves: ${total_cash:,.2f}", 0, 1)
            pdf.ln(5)

            # Embed Chart in PDF
            pdf.set_font("helvetica", "B", 13)
            pdf.cell(0, 8, "2. Visual Portfolio Chart", 0, 1)
            pdf.image(tmp_path, x=15, y=pdf.get_y(), w=180)
            pdf.ln(55)

            pdf.set_font("helvetica", "B", 13)
            pdf.cell(0, 8, "3. Accounts & Balances", 0, 1)
            pdf.set_font("helvetica", "", 11)
            if accounts:
                for acc in accounts:
                    pdf.cell(0, 6, f"- {acc['name']} ({acc['type']}): ${acc['balance']:,.2f}", 0, 1)
            else:
                pdf.cell(0, 6, "No accounts recorded.", 0, 1)
            pdf.ln(5)

            pdf_bytes = bytes(pdf.output())

            st.download_button(
                label="📥 Download Generated PDF File" if lang=="English" else "📥 Descargar Archivo PDF Generado",
                data=pdf_bytes,
                file_name=f"WealthSpark_Report_{st.session_state.current_user}.pdf",
                mime="application/pdf"
            )
            st.success("PDF Report generated successfully with embedded charts!" if lang=="English" else "¡Informe PDF generado con éxito con gráficos incorporados!")
        except Exception as e:
            st.error(f"Error generating PDF: {e}")
