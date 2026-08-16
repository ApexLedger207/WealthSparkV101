import streamlit as st
import pandas as pd
from database import save_user_data
from translations import t

CATEGORIES_EN = ["Salary", "Food", "Groceries", "Utilities", "Shopping", "Entertainment", "Other"]
CATEGORIES_ES = ["Salario", "Comida", "Supermercado", "Servicios", "Compras", "Entretenimiento", "Otro"]

def render(db, lang):
    st.markdown(f"<h1>📝 {t('transactions', lang)}</h1>", unsafe_allow_html=True)
    cats = CATEGORIES_EN if lang=="English" else CATEGORIES_ES
    
    with st.expander(f"➕ {t('record_tx', lang)}"):
        with st.form("tx_form"):
            tdate = st.date_input("Date" if lang=="English" else "Fecha")
            ttype = st.selectbox("Type" if lang=="English" else "Tipo", ["Expense", "Income"] if lang=="English" else ["Gasto", "Ingreso"])
            tcat = st.selectbox("Category" if lang=="English" else "Categoría", cats)
            tamt = st.number_input("Amount ($)" if lang=="English" else "Monto ($)", min_value=0.0, value=0.00, format="%.2f")
            tdesc = st.text_input("Description" if lang=="English" else "Descripción")
            if st.form_submit_button(t("save", lang)):
                db["transactions"].append({"date": str(tdate), "type": ttype, "category": tcat, "amount": tamt, "description": tdesc})
                save_user_data(st.session_state.current_user, db)
                st.success("Saved!" if lang=="English" else "¡Guardado!")
                st.rerun()

    if db["transactions"]:
        st.dataframe(pd.DataFrame(db["transactions"]), use_container_width=True)
        tidx = st.number_input("Delete Index" if lang=="English" else "Índice a Eliminar", min_value=0, max_value=max(0, len(db["transactions"])-1), step=1)
        if st.button(t("delete", lang)):
            db["transactions"].pop(int(tidx))
            save_user_data(st.session_state.current_user, db)
            st.rerun()
    else:
        st.info(t("no_data", lang))
