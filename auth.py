import streamlit as st
import secrets
import string
import hashlib

def generate_recovery_passkey(length=16):
    """Generates a secure, alphanumeric one-time passkey."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_passkey(passkey):
    """Hashes the passkey for secure database storage."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def generate_recovery_kit_content(username, passkey):
    """Formats the downloadable .txt recovery kit."""
    return f"""=========================================
WEALTHSPARK RECOVERY KIT
=========================================
Account: {username}
Recovery Passkey: {passkey}

KEEP THIS FILE SECURE. 
This passkey is the ONLY way to recover your account if you lose your password.
Do not share this key with anyone.
========================================="""

def render_auth_view():
    """Handles authentication, registration, and strict passkey recovery flows."""
    tab1, tab2, tab3 = st.tabs(["Login", "Register", "Recover Account"])
    
    with tab1:
        st.subheader("Sign In")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            # TODO: Validate credentials against SQLAlchemy backend
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Successfully logged in!")
            st.rerun()
            
    with tab2:
        st.subheader("Create Account")
        reg_username = st.text_input("Choose Username", key="reg_user")
        reg_password = st.text_input("Choose Password", type="password", key="reg_pass")
        
        if st.button("Register Account"):
            if reg_username and reg_password:
                raw_passkey = generate_recovery_passkey()
                # hashed_key = hash_passkey(raw_passkey) # Store this in your DB
                
                st.success("Account successfully created.")
                st.warning(f"Your One-Time Recovery Passkey is: **{raw_passkey}**")
                st.error("⚠️ Download your Recovery Kit now. This passkey will never be shown again.")
                
                kit_content = generate_recovery_kit_content(reg_username, raw_passkey)
                st.download_button(
                    label="⬇️ Download Recovery Kit (.txt)",
                    data=kit_content,
                    file_name=f"WealthSpark_Recovery_{reg_username}.txt",
                    mime="text/plain"
                )
                
    with tab3:
        st.subheader("Emergency Account Recovery")
        rec_username = st.text_input("Username", key="rec_user")
        passkey_input = st.text_input("Recovery Passkey", type="password", key="rec_passkey")
        new_password = st.text_input("New Password", type="password", key="rec_new_pass")
        
        if st.button("Reset Password"):
            # TODO: Validate passkey hash against DB stored hash
            if passkey_input: 
                st.success("Password reset successfully. Please store your newly generated recovery kit.")
            else:
                st.error("Invalid Recovery Passkey.")
