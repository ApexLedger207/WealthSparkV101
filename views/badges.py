import streamlit as st
from translations import t

def render(db, lang):
    st.markdown(f"<h1>🏆 {t('badges', lang)}</h1>", unsafe_allow_html=True)
    st.markdown("Unlock milestones automatically as you build wealth and eliminate debt!" if lang=="English" else "¡Desbloquea hitos automáticamente al construir riqueza y eliminar deudas!")

    accounts = db["accounts"]
    custom_assets = db["custom_assets"]
    custom_debts = db["custom_debts"]

    total_assets = sum(acc["balance"] for acc in accounts if acc["balance"] > 0) + sum(i["value"] for i in custom_assets)
    total_liab = sum(abs(acc["balance"]) for acc in accounts if acc["balance"] < 0 or acc["type"] in ["Credit Card", "Liability"]) + sum(i["balance"] for i in custom_debts)
    net_worth = total_assets - total_liab

    badges_list = [
        {"name": "🌱 First Step" if lang=="English" else "🌱 Primer Paso", "desc": "Created your WealthSpark V101 profile" if lang=="English" else "Creaste tu perfil de WealthSpark V101", "unlocked": True},
        {"name": "🛡️ Debt Free" if lang=="English" else "🛡️ Libre de Deudas", "desc": "Total liabilities equal $0" if lang=="English" else "Pasivos totales iguales a $0", "unlocked": total_liab == 0},
        {"name": "🥉 $100k Club", "desc": "Achieved Net Worth over $100,000" if lang=="English" else "Patrimonio neto superior a $100,000", "unlocked": net_worth >= 100000},
        {"name": "🥈 $250k Club", "desc": "Achieved Net Worth over $250,000" if lang=="English" else "Patrimonio neto superior a $250,000", "unlocked": net_worth >= 250000},
        {"name": "🥇 $500k Club", "desc": "Achieved Net Worth over $500,000" if lang=="English" else "Patrimonio neto superior a $500,000", "unlocked": net_worth >= 500000},
        {"name": "💎 $750k Club", "desc": "Achieved Net Worth over $750,000" if lang=="English" else "Patrimonio neto superior a $750,000", "unlocked": net_worth >= 750000},
        {"name": "👑 Millionaire" if lang=="English" else "👑 Millionario", "desc": "Achieved Net Worth over $1,000,000" if lang=="English" else "Patrimonio neto superior a $1,000,000", "unlocked": net_worth >= 1000000},
    ]

    cols = st.columns(2)
    for idx, b in enumerate(badges_list):
        with cols[idx % 2]:
            status = ("✅ UNLOCKED" if lang=="English" else "✅ DESBLOQUEADO") if b["unlocked"] else ("🔒 Locked" if lang=="English" else "🔒 Bloqueado")
            st.markdown(f"### {b['name']} ({status})")
            st.markdown(f"*{b['desc']}*")
            st.markdown("---")
