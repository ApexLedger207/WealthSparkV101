TRANSLATIONS = {
    "English": {
        "app_title": "WealthSpark 💎",
        "dashboard": "Dashboard", "accounts": "Accounts & Credit", "assets_debts": "Assets & Debts",
        "transactions": "Transactions", "live_markets": "Live Markets", "freedom_calc": "Financial Freedom",
        "badges": "Achievements & Badges", "ai_coach": "AI Financial Coach", "security": "Security & Privacy",
        "money_guide": "Money Management 101", "user_guide": "User Guide", "pdf_report": "PDF Report Generator",
        "social_hub": "Social Hub", "net_worth": "Net Worth", "total_assets": "Total Assets", "total_liab": "Total Liabilities", "total_cash": "Total Cash",
        "save_cloud": "💾 Save Database (Cloud)", "sign_out": "🚪 Sign Out", "language": "🌐 Language",
        "add_account": "Add New Account", "credit_health": "Credit Health",
        "add_asset": "Add Custom Asset", "add_debt": "Add Custom Debt", "record_tx": "Record Transaction",
        "security_settings": "Security Settings", "backup_prot": "Encrypted Backup & Data Protection",
        "danger_zone": "Danger Zone (Data Deletion)", "generate_pdf": "📥 Generate & Download PDF Report",
        "assets_vs_liab": "Assets vs Liabilities", "income_vs_exp": "Income vs Expenses",
        "no_data": "No data available.", "save": "Save", "delete": "Delete", "edit": "Edit"
    },
    "Spanish": {
        "app_title": "WealthSpark 💎",
        "dashboard": "Tablero", "accounts": "Cuentas y Crédito", "assets_debts": "Activos y Deudas",
        "transactions": "Transacciones", "live_markets": "Mercados en Vivo", "freedom_calc": "Libertad Financiera",
        "badges": "Insignias y Logros", "ai_coach": "Asesor Financiero IA", "security": "Seguridad y Privacidad",
        "money_guide": "Gestión de Dinero 101", "user_guide": "Guía de Usuario", "pdf_report": "Generador de Informes PDF",
        "social_hub": "Centro Social", "net_worth": "Patrimonio Neto", "total_assets": "Activos Totales", "total_liab": "Pasivos Totales", "total_cash": "Efectivo Total",
        "save_cloud": "💾 Guardar Base de Datos (Nube)", "sign_out": "🚪 Cerrar Sesión", "language": "🌐 Idioma",
        "add_account": "Agregar Nueva Cuenta", "credit_health": "Salud Crediticia",
        "add_asset": "Agregar Activo Personalizado", "add_debt": "Agregar Deuda Personalizada", "record_tx": "Registrar Transacción",
        "security_settings": "Configuración de Seguridad", "backup_prot": "Respaldo Cifrado y Protección",
        "danger_zone": "Zona de Peligro (Eliminación)", "generate_pdf": "📥 Generar y Descargar Informe PDF",
        "assets_vs_liab": "Activos vs Pasivos", "income_vs_exp": "Ingresos y Gastos",
        "no_data": "No hay datos disponibles.", "save": "Guardar", "delete": "Eliminar", "edit": "Editar"
    }
}

def t(key, lang="English"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["English"]).get(key, key)
