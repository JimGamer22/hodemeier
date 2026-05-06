import mailslurp_client
import streamlit as st

def create_inbox():
    # Konfiguration für MailSlurp
    configuration = mailslurp_client.Configuration()
    # Falls du den Key anders nennst, hier anpassen
    configuration.api_key['x-api-key'] = st.secrets.get("mailslurp", {}).get("API_KEY", "DEIN_KEY_FEHLT")

    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox = inbox_controller.create_inbox()
        return inbox.email_address, inbox.id