# notifications.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import streamlit as st
import config

def send_email_notification(to_email, subject, body):
    """Sends an email notification via free Gmail SMTP."""
    gmail_user = getattr(config, 'GMAIL_USER', "")
    gmail_pass = getattr(config, 'GMAIL_APP_PASSWORD', "")

    if not gmail_user or not gmail_pass or gmail_user.startswith("your_"):
        st.warning(f"⚠️ **Gmail Unconfigured:** Email to `{to_email}` could not be sent because `GMAIL_USER` or `GMAIL_APP_PASSWORD` is not set in `config.py`.")
        return False

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_pass)
            server.sendmail(gmail_user, to_email, msg.as_string())
        st.success(f"Email successfully dispatched to {to_email} via Gmail!")
        return True
    except Exception as e:
        st.error(f"SMTP Email Error: {e}")
        return False

def send_sms_notification(to_phone, message):
    """Sends a free mobile alert via Telegram Bot API (replaces paid SMS)."""
    bot_token = getattr(config, 'TELEGRAM_BOT_TOKEN', "")
    chat_id = getattr(config, 'TELEGRAM_CHAT_ID', "")

    if not bot_token or not chat_id or bot_token.startswith("your_"):
        st.warning(f"⚠️ **Telegram Unconfigured:** Mobile alert for `{to_phone}` could not be sent because Telegram credentials are not set in `config.py`.")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    formatted_message = f"📱 **WealthSpark Alert** (Target: `{to_phone}`)\n\n{message}"
    
    payload = {
        "chat_id": chat_id,
        "text": formatted_message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success("Alert successfully dispatched to your Telegram app!")
            return True
        else:
            st.error(f"Telegram API Error: {response.text}")
            return False
    except Exception as e:
        st.error(f"Telegram Connection Error: {e}")
        return False
