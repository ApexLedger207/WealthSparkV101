import streamlit as st
import re
import uuid
import random
from database import load_users, save_users, load_user_data, save_user_data
from datetime import datetime
from services.notification import send_email_notification, send_sms_notification

def validate_password(password):
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one capital letter (A-Z)."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number (0-9)."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character (!@#$%^&*...)."
    return None

def verify_user():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.current_user = None

    if st.session_state.authenticated:
        return True

    query_params = st.query_params
    if "activate" in query_params:
        token = query_params["activate"]
        users = load_users()
        for uname, udata in users.items():
            if udata.get("activation_token") == token:
                udata["activated"] = True
                save_users(users)
                st.success(f"Email successfully confirmed for '{uname}'! You are now logged in.")
                st.session_state.authenticated = True
                st.session_state.current_user = uname
                st.session_state.db = load_user_data(uname)
                st.rerun()

    st.markdown("<h2 style='text-align: center;'>💎 WealthSpark V101 Secure Access</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Private multi-user financial suite with robust verification & encrypted backups.</p>", unsafe_allow_html=True)
    
    tab_login, tab_register, tab_forgot = st.tabs(["Sign In", "Create Account", "Secure Recovery"])

    users = load_users()

    with tab_login:
        with st.form("login_form"):
            username_input = st.text_input("Username (Case-Sensitive)", value="admin")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign In")
            if submitted:
                matched_user = None
                for u in users:
                    if u == username_input.strip():
                        matched_user = u
                        break

                if matched_user and users[matched_user]["password"] == password:
                    if not users[matched_user].get("activated", False):
                        st.error("Account not activated! Please check your email inbox and click the activation link.")
                    else:
                        st.session_state.authenticated = True
                        st.session_state.current_user = matched_user
                        st.session_state.db = load_user_data(matched_user)
                        users[matched_user]["last_login"] = str(datetime.now())
                        users[matched_user]["audit_log"].append(f"[{datetime.now()}] User signed in.")
                        save_users(users)
                        st.success("Signed in successfully!")
                        st.rerun()
                else:
                    st.error("Invalid username or password. Default admin / Admin@1")

    with tab_register:
        with st.form("register_form"):
            st.markdown("Create your private account with security verification.")
            new_user = st.text_input("Choose Username (Case-Sensitive)")
            new_email = st.text_input("Email Address")
            new_phone = st.text_input("Phone Number (for SMS code recovery)")
            sec_q = st.selectbox("Security Question", [
                "What is your pet's name?",
                "What was your first car?",
                "In what city were you born?",
                "What is your favorite book?"
            ])
            sec_a = st.text_input("Secret Security Answer")
            new_pass = st.text_input("Choose Password", type="password")
            confirm_pass = st.text_input("Confirm Password", type="password")
            reg_sub = st.form_submit_button("Register Account")
            
            if reg_sub:
                if not new_user or not new_pass or not new_email or not new_phone or not sec_a:
                    st.error("Please fill in all required fields including phone number.")
                elif new_pass != confirm_pass:
                    st.error("Passwords do not match. Please re-enter confirmation.")
                else:
                    exists = any(u == new_user.strip() for u in users)
                    if exists:
                        st.error("Username already exists. Please choose another.")
                    else:
                        err = validate_password(new_pass)
                        if err:
                            st.error(err)
                        else:
                            token = str(uuid.uuid4())
                            clean_uname = new_user.strip()
                            users[clean_uname] = {
                                "password": new_pass,
                                "email": new_email.strip(),
                                "phone": new_phone.strip(),
                                "activated": False,
                                "activation_token": token,
                                "sec_question": sec_q,
                                "sec_answer": sec_a.strip().lower(),
                                "last_login": str(datetime.now()),
                                "audit_log": [f"[{datetime.now()}] Account registered. Pending confirmation."]
                            }
                            save_users(users)
                            save_user_data(clean_uname, load_user_data(clean_uname))
                            
                            st.success(f"Account '{clean_uname}' created successfully!")
                            send_email_notification(new_email, "Account Activation", f"Click to verify: /?activate={token}")
                            send_sms_notification(new_phone, f"Welcome to WealthSpark! Your verification token is {token[:6]}")
                            st.markdown(f"### 📧 Activation Link (Simulated Dispatch)")
                            st.markdown(f"> **Activation URL:** **[Activate Account & Auto-Login](/?activate={token})**")

    with tab_forgot:
        st.markdown("### Secure Multi-Factor Password Recovery")
        st.markdown("To prevent unauthorized resets, password recovery requires your exact Username, Email, Phone SMS verification code, and your Security Question answer.")

        if "recovery_step" not in st.session_state:
            st.session_state.recovery_step = 1
            st.session_state.rec_user = ""
            st.session_state.rec_sms_code = ""

        with st.form("forgot_step1"):
            f_user = st.text_input("Your Exact Username", value=st.session_state.rec_user)
            step1_sub = st.form_submit_button("Lookup Security Question")
            if step1_sub:
                matched_fuser = None
                for u in users:
                    if u == f_user.strip():
                        matched_fuser = u
                        break
                if matched_fuser:
                    st.session_state.rec_user = matched_fuser
                    st.session_state.recovery_step = 2
                    st.session_state.rec_sms_code = str(random.randint(100000, 999999))
                    st.success("Username found! Security question loaded.")
                    send_sms_notification(users[matched_fuser]["phone"], f"Your recovery SMS code is: {st.session_state.rec_sms_code}")
                    st.rerun()
                else:
                    st.error("Username not found in registry.")

        if st.session_state.recovery_step >= 2:
            matched_user_data = users.get(st.session_state.rec_user, {})
            current_sec_q = matched_user_data.get("sec_question", "Security Question")
            
            with st.form("forgot_step2"):
                st.markdown(f"**Your Registered Security Question:** `{current_sec_q}`")
                f_email = st.text_input("Registered Email Address")
                f_phone_code = st.text_input("Enter 6-Digit SMS Code Sent to Phone")
                f_ans = st.text_input("Your Secret Security Answer")
                f_new_pass = st.text_input("New Secure Password", type="password")
                forgot_sub = st.form_submit_button("Verify & Reset Password")
                
                if forgot_sub:
                    stored_email = matched_user_data.get("email", "")
                    stored_ans = matched_user_data.get("sec_answer", "")
                    
                    if (stored_email.lower() == f_email.strip().lower() and 
                        stored_ans == f_ans.strip().lower() and 
                        f_phone_code.strip() == st.session_state.rec_sms_code):
                        
                        err = validate_password(f_new_pass)
                        if err:
                            st.error(err)
                        else:
                            users[st.session_state.rec_user]["password"] = f_new_pass
                            users[st.session_state.rec_user]["audit_log"].append(f"[{datetime.now()}] Password reset via multi-factor SMS & Security Question verification.")
                            save_users(users)
                            st.session_state.recovery_step = 1
                            st.success("Password successfully reset! You can now sign in with your new password.")
                    else:
                        st.error("Verification failed: Email, Security Answer, or SMS Code is incorrect.")

    return False
