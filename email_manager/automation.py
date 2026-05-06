import streamlit as st
import pandas as pd
from .email_generator import create_inbox
from auth import get_gspread_client

def show_email_manager():
    st.title("📧 Email & Account Manager")
    
    client = get_gspread_client()
    if not client: return

    # Öffne das Sheet über die ID aus deinen Secrets
    sheet_id = st.secrets["sheets"]["email_sheet_id"]
    worksheet_name = st.secrets["sheets"]["email_worksheet"]
    sheet = client.open_by_key(sheet_id).worksheet(worksheet_name)

    if st.button("➕ Neues MailSlurp Postfach erstellen"):
        with st.spinner("Erstelle Inbox..."):
            email_addr, inbox_id = create_inbox()
            # In das GSheet schreiben
            sheet.append_row([email_addr, inbox_id, "Aktiv"])
            st.success(f"Erstellt: {email_addr}")

    st.subheader("Deine Accounts")
    data = sheet.get_all_records()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Noch keine Accounts vorhanden.")