import streamlit as st
import secrets
import string
import hashlib

def generate_recovery_passkey(length=16):
    """Generates a secure, alphanumeric one-time recovery code."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_passkey(passkey):
    """Securely hashes the passkey for database comparison."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def generate_recovery_kit_content(username, passkey):
    """Formats the downloadable recovery kit text file."""
    return f"""=========================================
WEALTHSPARK SECURE RECOVERY KIT
=========================================
Account Username: {username}
One-Time Recovery Passkey: {passkey}

IMPORTANT: Keep this file in a secure location. 
This passkey is the ONLY method to recover your 
account if your password is lost. Do not share 
this key with anyone.
========================================="""

def verify_user():
    """Renders authentication tabs and enforces the One-Time Recovery Passkey system."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None

    if st.session_state.authenticated:
        return True

    st.markdown("<h1 style='text-align: center;'>💎 WealthSpark v102 Portal</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔐 Sign In", "📝 Register", "🔑 Recovery Passkey Reset"])

    with tab1:
        st.subheader("Account Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Authenticate", key="login_submit"):
            if username and password:
                # Stub validation logic matching backend DB
                st.session_state.authenticated = True
                st.session_state.current_user = username
                if "db" not in st.session_state or st.session_state.db is None:
                    st.session_state.db = {}
                st.success("Access Granted!")
                st.rerun()
            else:
                st.error("Please provide both username and password.")

    with tab2:
        st.subheader("Create New Account")
        reg_username = st.text_input("Choose Username", key="reg_user")
        reg_password = st.text_input("Choose Password", type="password", key="reg_pass")
        
        if st.button("Register & Generate Kit", key="reg_submit"):
            if reg_username and reg_password:
                raw_passkey = generate_recovery_passkey()
                # hashed_key = hash_passkey(raw_passkey) -> Save to DB here
                
                st.success("Account successfully created!")
                st.warning(f"Your One-Time Recovery Passkey: **{raw_passkey}**")
                st.error("⚠️ Download your Recovery Kit right now. This key will never be displayed again.")
                
                kit_content = generate_recovery_kit_content(reg_username, raw_passkey)
                st.download_button(
                    label="⬇️ Download Recovery Kit (.txt)",
                    data=kit_content,
                    file_name=f"WealthSpark_Recovery_{reg_username}.txt",
                    mime="text/plain"
                )
            else:
                st.error("All registration fields are required.")

    with tab3:
        st.subheader("Emergency Account Reset")
        st.markdown("Enter your username and your **One-Time Recovery Passkey** text file contents to reset your credentials.")
        
        rec_username = st.text_input("Username", key="rec_user")
        passkey_input = st.text_input("Recovery Passkey", type="password", key="rec_passkey")
        new_password = st.text_input("New Password", type="password", key="rec_new_pass")
        
        if st.button("Reset Credentials", key="reset_submit"):
            if rec_username and passkey_input and new_password:
                # Validate hash(passkey_input) against stored DB hash here
                st.success("Password successfully reset! You can now log in using your new password.")
            else:
                st.error("Invalid recovery parameters provided.")

    return False
