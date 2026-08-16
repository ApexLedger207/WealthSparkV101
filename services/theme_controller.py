import streamlit as st
import plotly.graph_objects as go

THEMES = {
    "Light": {
        "bg_color": "#FFFFFF",
        "text_color": "#1E1E1E",
        "card_bg": "#F8F9FA",
        "border": "#E9ECEF",
        "plotly_template": "plotly_white"
    },
    "Dark": {
        "bg_color": "#0E1117",
        "text_color": "#FAFAFA",
        "card_bg": "#1E2127",
        "border": "#2D3139",
        "plotly_template": "plotly_dark"
    }
}

def inject_theme_css(theme_name="Dark"):
    """Injects dynamic CSS variables and overrides global backgrounds/text."""
    theme = THEMES.get(theme_name, THEMES["Dark"])
    
    css = f"""
    <style>
    :root {{
        --main-bg: {theme['bg_color']};
        --main-text: {theme['text_color']};
        --card-bg: {theme['card_bg']};
        --border-color: {theme['border']};
    }}
    .stApp {{
        background-color: var(--main-bg);
        color: var(--main-text);
    }}
    
    /* Mobile-First Dashboard Card Overhaul */
    @media (max-width: 768px) {{
        .block-container {{
            padding: 1rem !important;
        }}
    }}
    
    div[data-testid="metric-container"] {{
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    div[data-testid="metric-container"] > label {{
        font-size: 0.85rem !important;
        color: #8892B0 !important;
        text-transform: uppercase;
    }}
    div[data-testid="metric-container"] > div {{
        font-size: 1.75rem !important;
        font-weight: 700 !important;
        color: var(--main-text) !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def apply_dynamic_plot_theme(fig, theme_name="Dark"):
    """Ensures Plotly charts adapt to dark mode with visible axes and text."""
    template = THEMES.get(theme_name, THEMES["Dark"])["plotly_template"]
    fig.update_layout(template=template)
    
    if theme_name == "Dark":
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2D3139', color='#FAFAFA')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2D3139', color='#FAFAFA')
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FAFAFA')
        )
    return fig
