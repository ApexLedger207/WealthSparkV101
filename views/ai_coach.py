import streamlit as st
import pandas as pd
from translations import t

def render(db, lang):
    st.markdown(f"<h1>🤖 {t('ai_coach', lang)}</h1>", unsafe_allow_html=True)
    
    if not st.session_state.get("ai_privacy_enabled", True):
        st.warning("🔒 **Privacy Mode Active:** AI Financial Data Processing is disabled via your sidebar settings. Enable 'Enable AI Financial Data Processing' to view automated financial analysis and recommendations." if lang=="English" else "🔒 **Modo de Privacidad Activo:** El procesamiento de datos financieros por IA está desactivado.")
        return

    st.markdown("Your personal AI financial analyst evaluates your live financial data." if lang=="English" else "Tu analista financiero personal con IA evalúa tus datos en tiempo real.")

    accounts = db["accounts"]
    custom_assets = db["custom_assets"]
    custom_debts = db["custom_debts"]

    total_assets = sum(acc["balance"] for acc in accounts if acc["balance"] > 0) + sum(i["value"] for i in custom_assets)
    total_liab = sum(abs(acc["balance"]) for acc in accounts if acc["balance"] < 0 or acc["type"] in ["Credit Card", "Liability"]) + sum(i["balance"] for i in custom_debts)
    net_worth = total_assets - total_liab
    cash_total = sum(acc["balance"] for acc in accounts if acc["type"] in ["Cash", "Checking", "Savings"])

    score = 50
    if net_worth > 50000: score += 15
    if net_worth > 200000: score += 15
    if total_liab == 0: score += 10
    elif total_liab < total_assets * 0.2: score += 5
    if cash_total > 5000: score += 10
    score = min(100, max(10, score))

    st.metric("🧠 AI Wealth Health Score" if lang=="English" else "🧠 Puntaje de Salud Financiera IA", f"{score} / 100")

    st.markdown("---")
    st.subheader("💡 Tailored AI Recommendations" if lang=="English" else "💡 Recomendaciones Personalizadas de IA")

    insights = []
    if total_liab > 0:
        insights.append(f"⚠️ **Debt Alert:** You currently carry ${total_liab:,.2f} in liabilities." if lang=="English" else f"⚠️ **Alerta de Deuda:** Actualmente tienes ${total_liab:,.2f} en pasivos.")
    else:
        insights.append("🌟 **Debt-Free Status:** Outstanding! You have zero recorded debt." if lang=="English" else "🌟 **Libre de Deudas:** ¡Excelente! Tienes cero deudas registradas.")

    if cash_total < 3000:
        insights.append("💡 **Emergency Fund:** Liquid cash is below $3,000." if lang=="English" else "💡 **Fondo de Emergencia:** Tu efectivo líquido está por debajo de $3,000.")
    else:
        insights.append("✅ **Cash Reserves:** Your liquid cash buffer is healthy." if lang=="English" else "✅ **Reservas de Efectivo:** Tu colchón de efectivo es saludable.")

    for ins in insights:
        st.markdown(f"> {ins}")
        st.markdown("")
