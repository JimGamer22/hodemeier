import streamlit as st

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        return True

    st.title("🔒 Login")
    password = st.text_input("Passwort eingeben:", type="password")
    
    if st.button("Anmelden"):
        if password == "2244":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Falsches Passwort!")
    return False