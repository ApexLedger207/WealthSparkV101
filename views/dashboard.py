import streamlit as st
import pandas as pd
import plotly.express as px
from translations import t

def render(db, lang):
    st.markdown(f"<h1>📊 {t('dashboard', lang)}</h1>", unsafe_allow_html=True)

    accounts = db["accounts"]
    custom_assets = db["custom_assets"]
    custom_debts = db["custom_debts"]

    total_cash = sum(acc["balance"] for acc in accounts if acc["type"] in ["Cash", "Checking", "Savings"])
    other_accounts_assets = sum(acc["balance"] for acc in accounts if acc["balance"] > 0 and acc["type"] not in ["Cash", "Checking", "Savings"])
    total_custom_assets = sum(item["value"] for item in custom_assets)
    total_assets = total_cash + other_accounts_assets + total_custom_assets

    credit_cards_liability = sum(abs(acc["balance"]) for acc in accounts if acc["type"] in ["Credit Card", "Liability"] or acc["balance"] < 0)
    total_custom_debts = sum(item["balance"] for item in custom_debts)
    total_liabilities = credit_cards_liability + total_custom_debts

    net_worth = total_assets - total_liabilities

    col1, col2 = st.columns(2)
    with col1:
        st.metric(t("net_worth", lang), f"${net_worth:,.2f}")
        st.metric(t("total_cash", lang), f"${total_cash:,.2f}")
    with col2:
        st.metric(t("total_assets", lang), f"${total_assets:,.2f}")
        st.metric(t("total_liab", lang), f"${total_liabilities:,.2f}")

    st.markdown("---")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader(t("assets_vs_liab", lang))
        if total_assets > 0 or total_liabilities > 0:
            fig_pie = px.pie(
                names=["Assets", "Liabilities"] if lang=="English" else ["Activos", "Pasivos"],
                values=[max(0, total_assets), total_liabilities],
                hole=0.4,
                color_discrete_sequence=["#10b981", "#ef4444"]
            )
            fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=220)
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info(t("no_data", lang))

    with c2:
        st.subheader(t("income_vs_exp", lang))
        txs = db["transactions"]
        if txs:
            df_tx = pd.DataFrame(txs)
            type_grouped = df_tx.groupby("type")["amount"].sum().reset_index()
            fig_bar = px.bar(
                type_grouped, x="type", y="amount", color="type",
                text_auto=".2f", color_discrete_sequence=["#3b82f6", "#f59e0b"]
            )
            fig_bar.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=220, showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info(t("no_data", lang))
