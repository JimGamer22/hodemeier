import streamlit as st

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        return True

    # Centered login card
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align:center; margin-bottom: 2rem;'>
            <span style='font-size: 48px;'>🔴</span>
            <h2 style='margin: 8px 0 4px; font-weight: 600;'>Hodemeier Hub</h2>
            <p style='color: #888; font-size: 14px;'>Bitte anmelden</p>
        </div>
        """, unsafe_allow_html=True)

        password = st.text_input("Passwort", type="password", label_visibility="collapsed")

        if st.button("Anmelden →", use_container_width=True, type="primary"):
            correct = st.secrets["app"]["APP_PASSWORD"]  
            if password == correct:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Falsches Passwort.")

    return False
