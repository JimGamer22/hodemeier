import streamlit as st
from auth import check_password

# Imports aus den Unterordnern
from google_account_manager.automation import render_automation_tab
from apored_predictor.predictor import render_predictor_tab

st.set_page_config(page_title="Multi-Tool Hub", layout="wide")

def main():
    if not check_password():
        return

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Bereich wählen:", ["Account Automation", "ApoRed Predictor"])
    
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    # Module aufrufen
    if choice == "Account Automation":
        render_automation_tab()
    elif choice == "ApoRed Predictor":
        render_predictor_tab()

if __name__ == "__main__":
    main()