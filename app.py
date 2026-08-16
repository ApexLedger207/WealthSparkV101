import streamlit as st
import json
from auth import verify_user
from database import save_user_data
from translations import t

st.set_page_config(page_title="WealthSpark 💎 V101", page_icon="💎", layout="centered", initial_sidebar_state="expanded")

if not verify_user():
    st.stop()

if "lang" not in st.session_state:
    st.session_state.lang = "English"

lang = st.sidebar.selectbox("🌐 Language", ["English", "Spanish"], index=["English", "Spanish"].index(st.session_state.lang))
st.session_state.lang = lang

# Theme Controller
themes = {
    "Light": {"bg": "#f8fafc", "text": "#1e293b", "card": "#ffffff", "primary": "#4f46e5"},
    "Sky Blue": {"bg": "#f0f9ff", "text": "#0f172a", "card": "#ffffff", "primary": "#0284c7"},
    "Pinky": {"bg": "#fdf2f8", "text": "#500724", "card": "#ffffff", "primary": "#db2777"}
}

if "theme_choice" not in st.session_state:
    st.session_state.theme_choice = "Light"

theme_choice = st.sidebar.selectbox("🎨 Theme", list(themes.keys()), index=list(themes.keys()).index(st.session_state.theme_choice))
st.session_state.theme_choice = theme_choice
th = themes[theme_choice]

# AI Financial Data Privacy Toggle
if "ai_privacy_enabled" not in st.session_state:
    st.session_state.ai_privacy_enabled = True
st.session_state.ai_privacy_enabled = st.sidebar.checkbox("🔒 Enable AI Financial Data Processing", value=st.session_state.ai_privacy_enabled)

# Enforce dynamic theme styling & hide native theme options / hamburger menu elements
css_template = """
<style>
.stApp {
    background-color: __BG__ !important;
    color: __TEXT__ !important;
}
h1, h2, h3, h4, h5, h6, p, span, label, div {
    color: __TEXT__ !important;
}
div.stButton > button {
    background: __PRIMARY__;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
    font-weight: 600;
    width: 100%;
}
div.stButton > button:hover {
    opacity: 0.9;
    color: white;
}
#MainMenu {visibility: visible;}
footer {visibility: hidden;}
header {visibility: visible;}
</style>
"""

st.markdown(
    css_template.replace("__BG__", th['bg'])
                .replace("__TEXT__", th['text'])
                .replace("__PRIMARY__", th['primary']),
    unsafe_allow_html=True
)

st.sidebar.markdown(f"### {t('app_title', lang)}")
st.sidebar.markdown(f"User: **{st.session_state.current_user}**")

nav_options = [
    t("dashboard", lang),
    t("accounts", lang),
    t("assets_debts", lang),
    t("transactions", lang),
    t("live_markets", lang),
    t("freedom_calc", lang),
    t("badges", lang),
    t("ai_coach", lang),
    t("security", lang),
    t("social_hub", lang),
    t("money_guide", lang),
    t("user_guide", lang),
    t("pdf_report", lang)
]

if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = nav_options[0]

st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
for opt in nav_options:
    if st.sidebar.button(opt, key=f"nav_btn_{opt}"):
        st.session_state.nav_choice = opt
        st.rerun()

menu = st.session_state.nav_choice

st.sidebar.markdown("---")
if st.sidebar.button(t("save_cloud", lang)):
    save_user_data(st.session_state.current_user, st.session_state.db)
    st.sidebar.success("Database saved to cloud server backend!")

st.sidebar.markdown("---")
if st.sidebar.button(t("sign_out", lang)):
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.session_state.db = None
    st.rerun()

from views import dashboard, accounts, assets_debts, transactions, live_markets, freedom_calc, badges, ai_coach, security_settings, social_sharing, money_guide, user_guide, pdf_report

if menu == t("dashboard", lang):
    dashboard.render(st.session_state.db, lang)
elif menu == t("accounts", lang):
    accounts.render(st.session_state.db, lang)
elif menu == t("assets_debts", lang):
    assets_debts.render(st.session_state.db, lang)
elif menu == t("transactions", lang):
    transactions.render(st.session_state.db, lang)
elif menu == t("live_markets", lang):
    live_markets.render(lang)
elif menu == t("freedom_calc", lang):
    freedom_calc.render(st.session_state.db, lang)
elif menu == t("badges", lang):
    badges.render(st.session_state.db, lang)
elif menu == t("ai_coach", lang):
    ai_coach.render(st.session_state.db, lang)
elif menu == t("security", lang):
    security_settings.render(st.session_state.db, lang)
elif menu == t("social_hub", lang):
    social_sharing.render(lang)
elif menu == t("money_guide", lang):
    money_guide.render(lang)
elif menu == t("user_guide", lang):
    user_guide.render(lang)
elif menu == t("pdf_report", lang):
    pdf_report.render(st.session_state.db, lang)
