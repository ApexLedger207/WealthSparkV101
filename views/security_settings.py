import streamlit as st
from database import save_user_data, generate_encrypted_backup
from datetime import datetime
from translations import t

def render(db, lang):
    st.markdown(f"<h1>🔒 {t('security', lang)}</h1>", unsafe_allow_html=True)
    
    sec = db.get("security_settings", {})

    st.subheader("App Lock & PIN" if lang=="English" else "Bloqueo de Aplicación y PIN")
    with st.form("pin_form"):
        new_pin = st.text_input("Set 4-Digit Security PIN" if lang=="English" else "Establecer PIN de 4 Dígitos", type="password", max_chars=4)
        app_lock_toggle = st.checkbox("Enable App Lock" if lang=="English" else "Habilitar Bloqueo de App", value=sec.get("app_lock", False))
        if st.form_submit_button(t("save", lang)):
            sec["pin"] = new_pin
            sec["app_lock"] = app_lock_toggle
            db["security_settings"] = sec
            save_user_data(st.session_state.current_user, db)
            st.success("Updated!" if lang=="English" else "¡Actualizado!")
            st.rerun()

    st.markdown("---")
    st.subheader(t("backup_prot", lang))
    
    pin_required = sec.get("app_lock", False) and sec.get("pin", "") != ""
    auth_pin = ""
    if pin_required:
        auth_pin = st.text_input("Enter 4-Digit PIN to Authorize Sensitive Action" if lang=="English" else "Ingrese PIN para Autorizar", type="password", max_chars=4, key="backup_auth_pin")

    backup_pass = st.text_input("Encryption Password for Backup" if lang=="English" else "Contraseña de Cifrado para Respaldo", type="password", key="bk_pass")
    if st.button("Export Encrypted JSON Backup" if lang=="English" else "Exportar Respaldo Cifrado JSON"):
        if pin_required and auth_pin != sec.get("pin", ""):
            st.error("Incorrect security PIN! Authorization failed." if lang=="English" else "¡PIN incorrecto!")
        elif backup_pass:
            enc_str = generate_encrypted_backup(db, backup_pass)
            sec["last_backup_date"] = str(datetime.now())
            save_user_data(st.session_state.current_user, db)
            st.download_button(
                label="📥 Download Encrypted Backup File" if lang=="English" else "📥 Descargar Archivo Cifrado",
                data=enc_str,
                file_name=f"secure_backup_{st.session_state.current_user}.enc",
                mime="text/plain"
            )
            st.success("Success!" if lang=="English" else "¡Éxito!")
        else:
            st.error("Enter password." if lang=="English" else "Ingrese contraseña.")

    st.markdown("---")
    st.subheader(t("danger_zone", lang))
    confirm_danger = st.checkbox("I understand this permanently deletes data" if lang=="English" else "Entiendo que esto borra permanentemente los datos")
    
    del_auth_pin = ""
    if pin_required:
        del_auth_pin = st.text_input("Enter 4-Digit PIN to Confirm Deletion" if lang=="English" else "Ingrese PIN para Confirmar", type="password", max_chars=4, key="del_auth_pin")

    if st.button("🗑️ Delete My Personal Financial Records" if lang=="English" else "🗑️ Eliminar Mis Registros Financieros"):
        if pin_required and del_auth_pin != sec.get("pin", ""):
            st.error("Incorrect security PIN! Deletion aborted." if lang=="English" else "¡PIN incorrecto!")
        elif confirm_danger:
            db["accounts"] = []
            db["custom_assets"] = []
            db["custom_debts"] = []
            db["transactions"] = []
            save_user_data(st.session_state.current_user, db)
            st.warning("Wiped." if lang=="English" else "Borrado.")
            st.rerun()
        else:
            st.error("Please check confirmation box." if lang=="English" else "Marque la casilla.")
