import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import secrets
import string
import mailslurp_client

# Konfiguration (Key in st.secrets speichern!)
configuration = mailslurp_client.Configuration()
configuration.api_key['sk_tavEGouWaFotdCkE_bjAv0kTi84XmirM8NOhDVyDQy0AjnrZyp4JexYREqgiZNemUydiu4OIGYe1ejP4p'] = "DEIN_MAILSLURP_API_KEY"

def create_real_email():
    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        
        # Erstellt ein echtes Postfach
        inbox = inbox_controller.create_inbox_with_defaults()
        
        return {
            "email": inbox.email_address,
            "id": inbox.id
        }

# Beispiel-Nutzung:
# new_acc = create_real_email()
# print(f"Echte E-Mail erstellt: {new_acc['email']}")

def generate_secure_password(length=12):
    """Generiert ein sicheres Passwort."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for i in range(length))

def render_email_generator_tab():
    st.markdown("## 🆕 Email Account Creator")
    
    # Verbindung zu Google Sheets (um die erstellten Accounts zu loggen)
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # UI für die Erstellung
    with st.expander("🛠️ Neuen Account konfigurieren", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("Nutzername / Prefix", placeholder="z.B. max.mustermann")
            domain = st.selectbox("Domain auswählen", ["deine-domain.de", "shop-kunden.com", "test-umgebung.net"])
        with col2:
            password = st.text_input("Passwort", value=generate_secure_password())
            account_type = st.selectbox("Typ", ["Standard", "Admin", "Temporär"])

    if st.button("🚀 Account jetzt erstellen", type="primary", use_container_width=True):
        if not username:
            st.error("Bitte einen Nutzernamen eingeben.")
        else:
            full_email = f"{username}@{domain}"
            
            # --- LOGIK ZUR ERSTELLUNG HIER EINFÜGEN ---
            # HINWEIS: Hier müsste ein API-Aufruf zu deinem Provider erfolgen 
            # (z.B. IONOS API, Google Workspace Admin SDK, etc.)
            
            st.warning(f"Schnittstelle zu {domain} wird aufgerufen...")
            
            # Speichern der Daten im Google Sheet (Logging)
            new_account = pd.DataFrame([{
                "email": full_email,
                "password": password,
                "type": account_type,
                "status": "aktiv",
                "created_at": datetime.now().strftime("%d.%m.%Y %H:%M")
            }])
            
            try:
                # Hier laden wir die bestehenden Daten und hängen den neuen Account an
                existing_data = conn.read(worksheet="accounts", ttl=0)
                updated_df = pd.concat([existing_data, new_account], ignore_index=True)
                conn.update(worksheet="accounts", data=updated_df)
                
                st.success(f"✅ Account {full_email} wurde im System registriert!")
            except Exception as e:
                st.error(f"Fehler beim Speichern im Log: {e}")

    # Übersicht der erstellten Accounts
    st.markdown("---")
    st.markdown("### 📋 Erstellte Accounts")
    try:
        data = conn.read(worksheet="accounts", ttl=0)
        st.dataframe(data, use_container_width=True)
    except:
        st.info("Noch keine Accounts in der Datenbank.")
        