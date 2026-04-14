"""
Google Sheets Setup Script für Email Generator
Führe dieses Script einmalig aus, um die nötigen Worksheets zu erstellen.
"""

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Setup", layout="centered")

st.markdown("## 🔧 Hodemeier - Google Sheets Setup")

st.info("""
Dieses Script erstellt die notwendigen Worksheets in Google Sheets:
- `emails` - für den Email Generator
- `stats` - für ApoRed Predictor (falls nicht vorhanden)
""")

if st.button("⚙️  Setup durchführen", type="primary", use_container_width=True):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # Worksheet für Emails
        emails_df = pd.DataFrame(columns=[
            "email_id", "sender", "recipient", "recipient_name", "subject", 
            "body", "template", "status", "created_at", "sent_at"
        ])
        
        st.write("📧 Erstelle 'emails' Worksheet...")
        conn.update(worksheet="emails", data=emails_df)
        st.success("✅ 'emails' Worksheet erstellt")
        
        # Worksheet für Stats (ApoRed)
        stats_df = pd.DataFrame(columns=[
            "runde", "platz", "kills", "map", "win_vorher", "stunde"
        ])
        
        st.write("📊 Erstelle 'stats' Worksheet...")
        conn.update(worksheet="stats", data=stats_df)
        st.success("✅ 'stats' Worksheet erstellt")
        
        st.markdown("---")
        st.success("""
        ✅ **Setup erfolgreich!**
        
        Deine Google Sheets sind jetzt vorbereitet:
        - ✅ Worksheet 'emails' - Emails speichern
        - ✅ Worksheet 'stats' - ApoRed Statistiken
        
        Du kannst jetzt die normale App starten!
        """)
        
    except Exception as e:
        st.error(f"""
        ❌ **Fehler beim Setup:**
        
        {str(e)}
        
        **Lösungsansätze:**
        1. Überprüfe die Google Sheets Connection in `secrets.toml`
        2. Stelle sicher, dass die Spreadsheet-ID korrekt ist
        3. Prüfe die Berechtigung deines Google-Accounts
        """)
