import streamlit as st
from translations import t

def render(lang):
    st.markdown(f"<h1>💡 {t('money_guide', lang)}</h1>", unsafe_allow_html=True)
    if lang == "English":
        st.markdown("""
        Welcome to the **WealthSpark Personal Finance Education Center**. Mastering core financial principles is the bedrock of building long-term generational wealth and achieving absolute financial freedom. Below is your comprehensive guide to modern personal finance.

        ---

        ### 1. Understanding Your Accounts
        * **Checking Account:** Your day-to-day transaction hub for receiving income and paying bills. Keep only 1 to 2 months of expenses here.
        * **Savings Account:** A secure holding place for your short-term cash reserves and emergency buffer.
        * **Cash:** Physical currency or liquid holdings instantly accessible.
        * **Investment Accounts:** Brokerage accounts holding stocks, bonds, ETFs, and precious metals.
        > **What to do in WealthSpark:** Use **Accounts & Credit** to monitor all your bank accounts and credit health.

        ### 2. Assets vs. Liabilities & Net Worth
        * **Assets:** Anything you own that has economic value (cash, real estate, vehicles, gold bullion).
        * **Liabilities:** What you owe to others (credit card balances, mortgages, student loans).
        * **Net Worth:** Assets minus Liabilities. This is your true financial scoreboard.
        > **What to do in WealthSpark:** Use **Assets & Debts** to track physical assets and custom loans, updating your net worth automatically on the **Dashboard**.

        ### 3. Credit Cards & Debt Management
        * **Credit Cards:** Powerful payment tools if paid in full monthly, but dangerous if carrying high-interest revolving balances.
        * **Credit Utilization:** Keep your credit utilization below 30% (ideally under 10%) of your total limit to maintain an excellent credit score.
        * **Payment History:** The single biggest factor in your credit score. Never miss a due date.
        > **What to do in WealthSpark:** Monitor your credit score and utilization metrics under **Accounts & Credit**.

        ### 4. Golden Rules & Tips for Beginners
        * **50/30/20 Rule:** Allocate 50% of income to Needs, 30% to Wants, and 20% to Savings & Wealth. Remember, this is a helpful guideline, not a rigid law!
        * **Emergency Fund:** Always prioritize building a cash safety net before aggressive investing.
        * **Track Every Dollar:** Awareness is the first step toward financial control.
        * **Pay Yourself First:** Automate savings contributions the moment income hits your account.
        > **Quick Tip:** You don't need a perfect budget. You need a budget you can actually follow consistently.

        ---

        ### 5. 💰 Budgeting
        * **What a Budget Is:** A spending and saving plan based on your income and expenses.
        * **Needs vs. Wants:** Distinguish between absolute survival necessities (housing, food, healthcare) and discretionary lifestyle choices (dining out, luxury gadgets).
        * **Planned vs. Actual Spending:** Compare what you expected to spend against real-world transaction data to catch budget leaks early.
        > **What to do in WealthSpark:** Use **Transactions** to log daily expenses and categorize spending.

        ### 6. 📊 Cash Flow
        * **Income vs. Expenses:** Cash flow is positive when money coming in exceeds money going out. Positive cash flow fuels wealth accumulation.
        > **What to do in WealthSpark:** Check your monthly income vs. expense graphs on the **Dashboard**.

        ### 7. 🎯 Financial Goals
        * Set clear, realistic targets: emergency funds, paying off debt, saving for a home, or investing for retirement.
        > **What to do in WealthSpark:** Track your net worth milestones and unlock badges in **Achievements & Badges**.

        ### 8. 💳 Debt Payoff Strategies
        * **Debt Avalanche:** Pay off the highest interest rate debt first to save the most money mathematically.
        * **Debt Snowball:** Pay off the smallest balance first for quick psychological momentum.
        * **Minimum Payments:** Always pay minimums across all accounts while aggressively attacking your target debt.

        ### 9. 📈 Investing Basics
        * **Stocks, Bonds, ETFs, and Index Funds:** Diversification across asset classes lowers portfolio risk.
        * **Compound Growth:** Time in the market beats timing the market.
        > **What to do in WealthSpark:** Use **Live Markets** to monitor live commodity and index prices, and **Financial Freedom** to simulate compound growth. *(Note: Live Markets is not financial advice.)*

        ### 10. 🏦 Emergency Fund Essentials
        * Keep 3 to 6 months of essential living expenses in a High-Yield Savings Account (HYSA). Use strictly for true financial emergencies (job loss, medical crises).

        ### 11. 🧾 Bills & Subscriptions
        * Audit recurring subscriptions quarterly to eliminate unused monthly software, streaming, or membership drains.

        ### 12. 🛡️ Financial Safety & Security
        * Use strong passwords, enable two-factor authentication, beware of phishing scams, and export regular encrypted backups.
        > **What to do in WealthSpark:** Visit **Security & Privacy** to set app locks and export `.enc` backups.

        ### 13. 🏥 Insurance & 💵 Taxes Basics
        * Protect your hard-earned wealth with appropriate health, auto, home/renter's, and life insurance. Maintain organized financial records for hassle-free tax filing.

        ### 14. 📅 Monthly Financial Checkup Routine
        1. Review transactions and spending.
        2. Pay bills and check subscriptions.
        3. Update account balances and review debt.
        4. Check savings progress and investment growth.
        5. Export a secure database backup.
        """)
    else:
        st.markdown("""
        Bienvenido al **Centro de Educación Financiera Personal de WealthSpark**. Dominar los principios financieros básicos es la base para construir riqueza generacional a largo plazo y lograr la libertad financiera absoluta. A continuación se presenta su guía completa de finanzas personales.

        ---

        ### 1. Entendiendo Sus Cuentas
        * **Cuenta Corriente:** Su centro de transacciones diario para recibir ingresos y pagar facturas. Mantenga solo de 1 a 2 meses de gastos aquí.
        * **Cuenta de Ahorros:** Un lugar seguro para sus reservas de efectivo a corto plazo y colchón de emergencia.
        * **Efectivo:** Moneda física o tenencias líquidas accesibles al instante.
        * **Cuentas de Inversión:** Cuentas de corretaje que poseen acciones, bonos, ETFs y metales preciosos.
        > **Qué hacer en WealthSpark:** Use **Cuentas y Crédito** para monitorear todas sus cuentas bancarias y salud crediticia.

        ### 2. Activos vs. Pasivos y Patrimonio Neto
        * **Activos:** Todo lo que posee con valor económico (efectivo, bienes raíces, vehículos, lingotes de oro).
        * **Pasivos:** Lo que debe a otros (saldos de tarjetas de crédito, hipotecas, préstamos estudiantiles).
        * **Patrimonio Neto:** Activos menos Pasivos. Este es su verdadero marcador financiero.
        > **Qué hacer en WealthSpark:** Use **Activos y Deudas** para rastrear activos físicos y préstamos personalizados, actualizando su patrimonio neto automáticamente en el **Tablero**.

        ### 3. Tarjetas de Crédito y Gestión de Deudas
        * **Tarjetas de Crédito:** Herramientas de pago poderosas si se pagan en su totalidad mensualmente, pero peligrosas si acumulan saldos con altos intereses.
        * **Utilización de Crédito:** Mantenga su utilización por debajo del 30% (idealmente menos del 10%) de su límite total.
        * **Historial de Pagos:** El factor más importante en su puntaje crediticio. Nunca pase por alto una fecha de vencimiento.
        > **Qué hacer en WealthSpark:** Monitoree su puntaje crediticio y métricas de utilización en **Cuentas y Crédito**.

        ### 4. Reglas de Oro y Consejos para Principiantes
        * **Regla 50/30/20:** Asigne 50% a Necesidades, 30% a Deseos y 20% a Ahorros y Riqueza. ¡Recuerde que es una guía útil, no una ley rígida!
        * **Fondo de Emergencia:** Priorice siempre construir un colchón de efectivo antes de invertir agresivamente.
        * **Rastree Cada Dólar:** La conciencia es el primer paso hacia el control financiero.
        * **Páguese a Sí Mismo Primero:** Automatice las contribuciones de ahorro en cuanto los ingresos lleguen a su cuenta.
        > **Consejo Rápido:** No necesita un presupuesto perfecto. Necesita un presupuesto que pueda seguir consistentemente.

        ---

        ### 5. 💰 Presupuesto
        * **Qué es un Presupuesto:** Un plan de gastos y ahorros basado en sus ingresos y gastos.
        * **Necesidades vs. Deseos:** Distinga entre necesidades de supervivencia absoluta (vivienda, comida, salud) y opciones de estilo de vida discrecionales (cenas fuera, dispositivos de lujo).
        * **Gastos Previstos vs. Reales:** Compare lo que esperaba gastar frente a los datos de transacciones del mundo real para detectar fugas presupuestarias a tiempo.
        > **Qué hacer en WealthSpark:** Use **Transacciones** para registrar gastos diarios y categorizar el gasto.

        ### 6. 📊 Flujo de Efectivo
        * **Ingresos vs. Gastos:** El flujo de efectivo es positivo cuando el dinero que entra supera al dinero que sale.
        > **Qué hacer en WealthSpark:** Revise sus gráficos mensuales de ingresos vs. gastos en el **Tablero**.

        ### 7. 🎯 Metas Financieras
        * Establezca objetivos claros y realistas: fondos de emergencia, pago de deudas, ahorro para vivienda o inversión para la jubilación.
        > **Qué hacer en WealthSpark:** Rastree hitos de patrimonio neto y desbloquee insignias en **Insignias y Logros**.

        ### 8. 💳 Estrategias de Liquidación de Deudas
        * **Avalancha de Deudas:** Pague primero la deuda con la tasa de interés más alta para ahorrar la mayor cantidad de dinero.
        * **Bola de Nieve de Deudas:** Pague primero el saldo más pequeño para obtener impulso psicológico rápido.

        ### 9. 📈 Conceptos Básicos de Inversión
        * **Acciones, Bonos, ETFs y Fondos Indexados:** La diversificación reduce el riesgo de la cartera.
        * **Crecimiento Compuesto:** El tiempo en el mercado supera a intentar cronometrar el mercado.
        > **Qué hacer en WealthSpark:** Use **Mercados en Vivo** para monitorear precios de materias primas e índices, y **Libertad Financiera** para simular crecimiento compuesto. *(Nota: Mercados en Vivo no es asesoramiento financiero.)*

        ### 10. 🏦 Esenciales del Fondo de Emergencia
        * Mantenga de 3 a 6 meses de gastos de subsistencia esenciales en una Cuenta de Ahorros de Alto Rendimiento (HYSA).

        ### 11. 🧾 Facturas y Suscripciones
        * Audite las suscripciones recurrentes trimestralmente para eliminar fugas mensuales innecesarias.

        ### 12. 🛡️ Seguridad y Privacidad Financiera
        * Utilice contraseñas seguras, habilite la autenticación de dos factores, desconfíe de estafas de phishing y exporte respaldos cifrados con regularidad.
        > **Qué hacer en WealthSpark:** Visite **Seguridad y Privacidad** para configurar bloqueos de aplicaciones y exportar respaldos `.enc`.

        ### 13. 🏥 Seguros y 💵 Conceptos Básicos de Impuestos
        * Proteja su riqueza ganada con esfuerzo con seguros adecuados de salud, auto, hogar/inquilino y vida. Mantenga registros financieros organizados para la declaración de impuestos.

        ### 14. 📅 Rutina de Revisión Financiera Mensual
        1. Revise transacciones y gastos.
        2. Pague facturas y verifique suscripciones.
        3. Actualice saldos de cuentas y revise deudas.
        4. Verifique el progreso de ahorros y crecimiento de inversiones.
        5. Exporte un respaldo seguro de la base de datos.
        """)
