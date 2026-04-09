import streamlit as st
from auth import check_password
from google_manager.automation import render_automation_tab
from apored.predictor import render_predictor_tab

# Seite konfigurieren
st.set_page_config(page_title="Multi-Tool Hub", layout="wide")

def main():
    # 1. Passwort-Check
    if not check_password():
        st.stop() # Stoppt die Ausführung hier, wenn nicht eingeloggt

    # 2. Navigation
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Bereich wählen:", ["Google Account Manager", "ApoRed Predictor"])
    
    st.sidebar.divider()
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    # 3. Content laden
    if choice == "Google Account Manager":
        render_automation_tab()
    elif choice == "ApoRed Predictor":
        render_predictor_tab()

if __name__ == "__main__":
    main()