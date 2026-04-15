import streamlit as st

def render_automation_tab():
    st.markdown("## 📧 Google Account Manager")
    st.info(
        "**Hinweis:** Playwright-Automation läuft nicht auf Streamlit Cloud.\n\n"
        "Für Gmail-Zugriff auf bestehende Accounts: **Gmail API** via `google-api-python-client`.\n\n"
        "Neue Google-Accounts lassen sich nicht automatisch erstellen (Terms of Service).",
        icon="ℹ️",
    )

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Account hinzufügen")
        email = st.text_input("Google Email", placeholder="name@gmail.com")
        if st.button("💾  Speichern", type="primary"):
            if email:
                st.success(f"Account **{email}** registriert.")
            else:
                st.warning("Bitte eine Email eingeben.")

    with col2:
        st.markdown("#### Gespeicherte Accounts")
        st.markdown("_Noch keine Accounts gespeichert._")
