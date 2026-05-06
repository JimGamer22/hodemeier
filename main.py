import streamlit as st
from apored_predictor.predictor import show_apored_predictor
from email_manager.automation import show_email_manager

# Login Logik
def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        pwd = st.text_input("Passwort eingeben", type="password")
        if st.button("Login"):
            if pwd == st.secrets["app"]["APP_PASSWORD"]:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Falsches Passwort!")
        return False
    return True

def main():
    st.set_page_config(page_title="Hodemeier Hub", layout="wide")

    if not check_password():
        return

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Projekt wählen:", ["ApoRed Predictor", "Email Manager"])
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    if choice == "ApoRed Predictor":
        show_apored_predictor()
    else:
        show_email_manager()

if __name__ == "__main__":
    main()
