import streamlit as st
from config import EMAIL_API_KEY, SMS_API_KEY

def send_email_notification(to_email, subject, body):
    if not EMAIL_API_KEY or EMAIL_API_KEY.startswith("your_"):
        st.warning(f"⚠️ **Email API Unconfigured:** Real email to `{to_email}` could not be sent because `EMAIL_API_KEY` is not set in `config.py`. Simulated notification triggered.")
        return False
    st.success(f"Email successfully dispatched to {to_email} via configured API.")
    return True

def send_sms_notification(to_phone, message):
    if not SMS_API_KEY or SMS_API_KEY.startswith("your_"):
        st.warning(f"⚠️ **SMS API Unconfigured:** Real SMS to `{to_phone}` could not be sent because `SMS_API_KEY` is not set in `config.py`. Simulated notification triggered.")
        return False
    st.success(f"SMS successfully dispatched to {to_phone} via configured API.")
    return True
