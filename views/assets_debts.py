import streamlit as st
from database import save_user_data
from translations import t

def render(db, lang):
    st.markdown(f"<h1>🏠 {t('assets_debts', lang)}</h1>", unsafe_allow_html=True)
    with st.expander(f"➕ {t('add_asset', lang)}"):
        with st.form("add_casset"):
            aname = st.text_input("Asset Name (e.g. Car, Gold Bullion)" if lang=="English" else "Nombre del Activo (ej. Auto, Oro)")
            aval = st.number_input("Value ($)" if lang=="English" else "Valor ($)", value=0.0, format="%.2f")
            if st.form_submit_button(t("save", lang)) and aname:
                db["custom_assets"].append({"name": aname, "value": aval})
                save_user_data(st.session_state.current_user, db)
                st.rerun()

    if db["custom_assets"]:
        for idx, item in enumerate(db["custom_assets"]):
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{item['name']}**: ${item['value']:,.2f}")
            if c2.button(t("delete", lang), key=f"del_ast_{idx}"):
                db["custom_assets"].pop(idx)
                save_user_data(st.session_state.current_user, db)
                st.rerun()

    st.markdown("---")
    with st.expander(f"➕ {t('add_debt', lang)}"):
        with st.form("add_cdebt"):
            dname = st.text_input("Debt Name (e.g. Mortgage, Loan)" if lang=="English" else "Nombre de Deuda (ej. Hipoteca, Préstamo)")
            dbal = st.number_input("Balance ($)" if lang=="English" else "Saldo ($)", value=0.0, format="%.2f")
            if st.form_submit_button(t("save", lang)) and dname:
                db["custom_debts"].append({"name": dname, "balance": dbal})
                save_user_data(st.session_state.current_user, db)
                st.rerun()

    if db["custom_debts"]:
        for idx, item in enumerate(db["custom_debts"]):
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{item['name']}**: ${item['balance']:,.2f}")
            if c2.button(t("delete", lang), key=f"del_dbt_{idx}"):
                db["custom_debts"].pop(idx)
                save_user_data(st.session_state.current_user, db)
                st.rerun()
