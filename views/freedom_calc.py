import streamlit as st
import pandas as pd
import plotly.express as px
from translations import t

def render(db, lang):
    st.markdown(f"<h1>🚀 {t('freedom_calc', lang)}</h1>", unsafe_allow_html=True)
    st.markdown("Simulate compound investment growth over time." if lang=="English" else "Simule el crecimiento de inversiones a plazo compuesto.")

    col1, col2 = st.columns(2)
    with col1:
        initial = st.number_input("Initial Lump Sum Investment ($)" if lang=="English" else "Inversión Inicial ($)", value=5000.0, step=500.0)
        monthly = st.number_input("Monthly Contribution ($)" if lang=="English" else "Aporte Mensual ($)", value=500.0, step=50.0)
    with col2:
        return_rate = st.slider("Expected Annual Return (%)" if lang=="English" else "Retorno Anual Esperado (%)", 1.0, 20.0, 8.0)
        years = st.slider("Time Horizon (Years)" if lang=="English" else "Horizonte de Tiempo (Años)", 1, 40, 10)

    data = []
    total = initial
    for y in range(years + 1):
        data.append({"Year" if lang=="English" else "Año": y, "Portfolio Value" if lang=="English" else "Valor del Portafolio": total})
        for _ in range(12):
            total = (total + monthly) * (1 + (return_rate / 100.0) / 12.0)

    df_proj = pd.DataFrame(data)
    st.markdown(f"### Projected Portfolio Value in {years} Years: **${df_proj.iloc[-1]['Portfolio Value' if lang=='English' else 'Valor del Portafolio']:,.2f}**")

    fig = px.area(df_proj, x=df_proj.columns[0], y=df_proj.columns[1], title="Compound Growth Trajectory" if lang=="English" else "Trayectoria de Crecimiento Compuesto", color_discrete_sequence=["#10b981"])
    st.plotly_chart(fig, use_container_width=True)
