import streamlit as st
from translations import t

def render(lang):
    st.markdown(f"<h1>🌐 {t('social_hub', lang)}</h1>", unsafe_allow_html=True)
    st.markdown("Share WealthSpark V101 across your favorite platforms and communities instantly." if lang=="English" else "Comparte WealthSpark V101 en tus plataformas y comunidades favoritas al instante.")

    st.markdown("### 📢 Social Media & Communities")
    
    platforms = [
        {"name": "Instagram", "icon": "📸", "url": "https://www.instagram.com/"},
        {"name": "WhatsApp", "icon": "💬", "url": "https://api.whatsapp.com/send?text=Check%20out%20WealthSpark%20Financial%20Suite!"},
        {"name": "TikTok", "icon": "🎵", "url": "https://www.tiktok.com/"},
        {"name": "Snapchat", "icon": "👻", "url": "https://www.snapchat.com/"},
        {"name": "X (Twitter)", "icon": "✖️", "url": "https://twitter.com/intent/tweet?text=Managing%20my%20finances%20with%20WealthSpark!%20%F0%9F%92%8E"},
        {"name": "Facebook", "icon": "📘", "url": "https://www.facebook.com/sharer/sharer.php?"},
        {"name": "LinkedIn", "icon": "💼", "url": "https://www.linkedin.com/sharing/share-offsite/?"},
        {"name": "Telegram", "icon": "✈️", "url": "https://t.me/share/url?url=&text=Check%20out%20WealthSpark!"},
        {"name": "Hacker News", "icon": "🟠", "url": "https://news.ycombinator.com/"},
        {"name": "Forum", "icon": "💬", "url": "#"}
    ]

    cols = st.columns(2)
    for idx, p in enumerate(platforms):
        with cols[idx % 2]:
            st.markdown(f"**{p['icon']} {p['name']}**")
            st.markdown(f"[Open {p['name']} Share Link]({p['url']})")
            st.markdown("---")
