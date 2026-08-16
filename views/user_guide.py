import streamlit as st
from translations import t

def render(lang):
    st.markdown(f"<h1>📖 {t('user_guide', lang)}</h1>", unsafe_allow_html=True)
    if lang == "English":
        st.markdown("""
        Welcome to **WealthSpark V101**. This comprehensive master guide walks you through every feature, sharing protocol, security workflow, and navigation tab in your private financial suite.

        ---

        ### 1. Sharing This Software With Friends & Family
        * **Can I share a link with anyone?** Yes! Once your app is deployed online (such as on Streamlit Community Cloud), you can simply copy and share your public web app URL link with anyone you choose.
        * **Do guests need GitHub or Streamlit accounts?** No! Your friends and family do not need to know anything about GitHub, Streamlit, or have accounts on those websites. When they open your shared link, they will see the secure sign-in page, click **Create Account**, enter their own username and password, and instantly get their own isolated, private financial workspace.

        ### 2. Understanding the Top-Right Menu (`...` Button)
        In the top-right corner of your Streamlit app interface, you will see a small menu icon (`...`). Here is what each option does:
        * **Theme / System Settings:** Controlled via the sidebar Theme Controller (Light, Sky Blue, Pinky).
        * **Rerun (Shortcut: R):** Instantly re-executes the Python script to refresh the app state.
        * **Clear Cache (Shortcut: C):** Clears any cached data or functions in memory.
        * **Print / Record Screen:** Built-in browser utilities to print your active screen view or record a session.
        * **Streamlit Version Info:** Displays the active Streamlit engine version running your app.

        ### 3. User Privacy & Multi-User Access
        * **Isolated Data:** Each user account has a completely private database file (`db_username.json`). Even the administrator cannot view or access another user's financial accounts or transaction history.
        * **Case-Sensitive Usernames:** When registering or signing in, note that usernames are case-sensitive.
        * **Sign In / Sign Out:** Use the Sign Out button in the sidebar to securely log out of your session.

        ### 4. Backup & Data Restoration
        * **Export Encrypted Backup:** Exports your exact financial records into an encrypted `.enc` backup file protected by your password.
        * **Data Protection:** Use the Security tab to manage app lock PINs and data deletion zones safely.

        ### 5. App Tabs Overview
        * **📊 Dashboard:** High-level executive summary of Net Worth, Cash, Assets, Liabilities, and comparison charts.
        * **💳 Accounts & Credit:** Manage bank checking, savings, cash, credit cards, and credit health metrics.
        * **🏠 Assets & Debts:** Track physical assets (vehicles, gold bullion) and custom debts/loans.
        * **📝 Transactions:** Log income and expenses with categories.
        * **📈 Live Markets:** Real-time pricing trends for Gold, Silver, Crude Oil, Bitcoin, and the S&P 500 via Yahoo Finance.
        * **🚀 Financial Freedom:** Compound growth investment simulator across custom time horizons.
        * **🏆 Achievements & Badges:** Automatically unlock milestones as net worth climbs and debt drops.
        * **🤖 AI Financial Coach:** Receive automated AI wealth scores and tailored recommendations (with privacy toggle).
        * **🔒 Security & Privacy:** PIN locks, encrypted backups, and safety controls.
        * **🌐 Social Hub:** Share WealthSpark across 10 major social platforms and communities instantly.
        * **💡 Money Management 101:** Educational master guide covering 14 pillars of personal finance.
        * **📖 User Guide:** You are here! Complete reference documentation.
        * **📄 PDF Report Generator:** Export a clean financial executive summary into a downloadable PDF report with embedded Matplotlib charts.
        """)
    else:
        st.markdown("""
        Bienvenido a **WealthSpark V101**. Esta guía maestra completa lo guía a través de cada función, protocolo de compartir, flujo de trabajo de seguridad y pestaña de navegación en su suite financiera privada.

        ---

        ### 1. Compartir Este Software con Amigos y Familiares
        * **¿Puedo compartir un enlace con cualquier persona?** ¡Sí! Una vez que su aplicación esté implementada en línea, simplemente puede copiar y compartir su URL pública.
        * **¿Los invitados necesitan cuentas de GitHub o Streamlit?** ¡No! Sus amigos y familiares no necesitan saber nada sobre GitHub o Streamlit. Al abrir el enlace compartido, verán la página de inicio de sesión segura, harán clic en **Crear Cuenta** y obtendrán instantáneamente su propio espacio de trabajo privado e aislado.

        ### 2. Entendiendo el Menú Superior Derecho (Botón `...`)
        En la esquina superior derecha de la interfaz de Streamlit, verá un icono de menú (`...`):
        * **Configuración de Tema:** Controlado mediante el selector de temas en la barra lateral.
        * **Rerun (Atajo: R):** Reejecuta instantáneamente el script de Python.
        * **Clear Cache (Atajo: C):** Borra los datos almacenados en caché.
        * **Imprimir / Grabar Pantalla:** Utilidades del navegador integradas.
        * **Información de Versión:** Muestra la versión activa de Streamlit.

        ### 3. Privacidad del Usuario y Acceso Multi-Usuario
        * **Datos Aislados:** Cada cuenta de usuario tiene un archivo de base de datos completamente privado (`db_username.json`).
        * **Nombres de Usuario Sensibles a Mayúsculas:** Tenga en cuenta que los nombres de usuario distinguen mayúsculas y minúsculas.
        * **Cerrar Sesión:** Use el botón Cerrar Sesión en la barra lateral.

        ### 4. Respaldo y Restauración de Datos
        * **Exportar Respaldo Cifrado:** Exporta sus registros financieros en un archivo `.enc` cifrado protegido por contraseña.

        ### 5. Resumen de Pestañas de la Aplicación
        * **📊 Tablero:** Resumen ejecutivo de alto nivel del patrimonio neto, efectivo, activos y pasivos.
        * **💳 Cuentas y Crédito:** Administre cuentas bancarias y puntaje crediticio.
        * **🏠 Activos y Deudas:** Rastree activos físicos y deudas personalizadas.
        * **📝 Transacciones:** Registre ingresos y gastos con categorías.
        * **📈 Mercados en Vivo:** Precios en tiempo real para Oro, Plata, Petróleo, Bitcoin y S&P 500.
        * **🚀 Libertad Financiera:** Simulador de crecimiento compuesto de inversiones.
        * **🏆 Insignias y Logros:** Desbloquee hitos automáticamente.
        * **🤖 Asesor Financiero IA:** Reciba puntajes y recomendaciones de IA.
        * **🔒 Seguridad y Privacidad:** Bloqueos PIN y respaldos cifrados.
        * **🌐 Centro Social:** Comparta WealthSpark en 10 plataformas sociales.
        * **💡 Gestión de Dinero 101:** Guía educativa de 14 pilares financieros.
        * **📖 Guía de Usuario:** ¡Está aquí! Documentación de referencia completa.
        * **📄 Generador de Informes PDF:** Exporte un resumen ejecutivo en PDF con gráficos de Matplotlib incorporados.
        """)
