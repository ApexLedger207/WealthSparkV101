import streamlit as st
import pandas as pd
from database import save_user_data
from translations import t

def render(db, lang):
    st.markdown(f"<h1>💳 {t('accounts', lang)}</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Accounts Manager" if lang=="English" else "Gestor de Cuentas", t("credit_health", lang)])

    with tab1:
        with st.expander(f"➕ {t('add_account', lang)}"):
            with st.form("add_acc_form"):
                acc_name = st.text_input("Account Name" if lang=="English" else "Nombre de Cuenta")
                acc_type = st.selectbox("Account Type" if lang=="English" else "Tipo de Cuenta", ["Checking" if lang=="English" else "Corriente", "Savings" if lang=="English" else "Ahorros", "Cash" if lang=="English" else "Efectivo", "Credit Card" if lang=="English" else "Tarjeta de Crédito", "Investment" if lang=="English" else "Inversión", "Liability" if lang=="English" else "Pasivo"])
                acc_bal = st.number_input("Balance ($)" if lang=="English" else "Saldo ($)", value=0.00, format="%.2f")
                if st.form_submit_button(t("save", lang)) and acc_name:
                    db["accounts"].append({"name": acc_name, "type": acc_type, "balance": acc_bal})
                    save_user_data(st.session_state.current_user, db)
                    st.success("Saved!" if lang=="English" else "¡Guardado!")
                    st.rerun()

        if db["accounts"]:
            for idx, acc in enumerate(db["accounts"]):
                c1, c2, c3 = st.columns([2, 2, 1])
                c1.markdown(f"**{acc['name']}**<br><span style='font-size: 0.85rem;'>{acc['type']}</span>", unsafe_allow_html=True)
                c2.markdown(f"**${acc['balance']:,.2f}**")
                if c3.button("🗑️", key=f"del_acc_{idx}"):
                    db["accounts"].pop(idx)
                    save_user_data(st.session_state.current_user, db)
                    st.rerun()
                st.markdown("---")
        else:
            st.info(t("no_data", lang))

    with tab2:
        ch = db["credit_health"]
        c1, c2, c3 = st.columns(3)
        c1.metric("Credit Score" if lang=="English" else "Puntaje Crediticio", ch.get("score", 720))
        c2.metric("Utilization" if lang=="English" else "Utilización", f"{ch.get('utilization', 12.0)}%")
        c3.metric("Payment History" if lang=="English" else "Historial de Pagos", f"{ch.get('payment_history', 100.0)}%")

        with st.form("update_credit_form"):
            new_score = st.number_input("Credit Score" if lang=="English" else "Puntaje Crediticio", min_value=0, max_value=850, value=int(ch.get("score", 720)))
            new_util = st.number_input("Utilization (%)" if lang=="English" else "Utilización (%)", min_value=0.0, max_value=100.0, value=float(ch.get("utilization", 12.0)))
            new_pay = st.number_input("Payment History (%)" if lang=="English" else "Historial de Pagos (%)", min_value=0.0, max_value=100.0, value=float(ch.get("payment_history", 100.0)))
            if st.form_submit_button(t("save", lang)):
                db["credit_health"] = {"score": new_score, "utilization": new_util, "payment_history": new_pay}
                save_user_data(st.session_state.current_user, db)
                st.success("Updated!" if lang=="English" else "¡Actualizado!")
                st.rerun()
