import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from translations import t

def render(lang):
    st.markdown(f"<h1>📈 {t('live_markets', lang)}</h1>", unsafe_allow_html=True)
    st.markdown("⚠️ *Note: The Live Markets section shows real-time market prices for informational purposes and is NOT financial advice.*" if lang=="English" else "⚠️ *Nota: La sección de Mercados en Vivo muestra precios en tiempo real con fines informativos y NO constituye asesoramiento financiero.*")
    
    tickers = {
        "Gold": "GC=F",
        "Silver": "SI=F",
        "Brent Crude Oil": "BZ=F",
        "Bitcoin": "BTC-USD",
        "S&P 500": "^GSPC"
    }

    for name, symbol in tickers.items():
        st.markdown(f"### {name} (`{symbol}`)")
        try:
            tk = yf.Ticker(symbol)
            info = tk.info
            hist = tk.history(period="1y")
            
            curr_price = info.get("currentPrice", info.get("regularMarketPrice", 0.0))
            if not curr_price and not hist.empty:
                curr_price = hist['Close'].iloc[-1]

            prev_close = info.get("previousClose", 0.0)
            change = curr_price - prev_close if prev_close else 0.0
            pct_change = (change / prev_close) * 100 if prev_close else 0.0
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Current Price" if lang=="English" else "Precio Actual", f"${curr_price:,.2f}", f"{change:+.2f} ({pct_change:+.2f}%)")
            c2.metric("Currency" if lang=="English" else "Moneda", info.get("currency", "USD"))
            c3.metric("Day Open" if lang=="English" else "Apertura Día", f"${info.get('open', 0.0):,.2f}")
            c4.metric("Volume" if lang=="English" else "Volumen", f"{info.get('volume', 0):,}")

            if not hist.empty:
                fig = px.line(hist, x=hist.index, y="Close", title=f"{name} - 52W Trend", color_discrete_sequence=["#4f46e5"])
                fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), height=220, xaxis_title="Date" if lang=="English" else "Fecha", yaxis_title="Price" if lang=="English" else "Precio")
                st.plotly_chart(fig, use_container_width=True)
        except Exception:
            st.warning("Live data temporarily unavailable." if lang=="English" else "Datos en vivo temporalmente no disponibles.")
        st.markdown("---")
