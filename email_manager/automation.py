import streamlit as st
import mailslurp_client

# email_manager/automation.py (Vorschlag)
def get_verification_code(inbox_id, search_term):
    configuration = mailslurp_client.Configuration()
    configuration.api_key['sk_tavEGouWaFotdCkE_bjAv0kTi84XmirM8NOhDVyDQy0AjnrZyp4JexYREqgiZNemUydiu4OIGYe1ejP4p'] = st.secrets["mailslurp"]["api_key"]

    with mailslurp_client.ApiClient(configuration) as api_client:
        wait_controller = mailslurp_client.WaitForControllerApi(api_client)
        # Wartet auf die nächste Email
        email = wait_controller.wait_for_latest_email(inbox_id=inbox_id, timeout=30000, unread_only=True)
        return email.body
    
    
    
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
