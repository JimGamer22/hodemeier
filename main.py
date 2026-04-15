import streamlit as st
from auth import check_password
from email_manager.automation import render_automation_tab
from apored_predictor.predictor import render_predictor_tab
from email_generator.email_generator import render_email_generator_tab

st.set_page_config(
    page_title="Hodemeier Hub",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: #111111;
        border-right: 1px solid #2a2a2a;
    }
    [data-testid="stSidebar"] * { color: #d0d0d0 !important; }
    [data-testid="stSidebar"] .stRadio label {
        padding: 10px 14px;
        border-radius: 8px;
        display: block;
        cursor: pointer;
        font-size: 14px;
    }
    [data-testid="stSidebar"] .stRadio label:hover { background: #1e1e1e; }
    .block-container { padding-top: 1.5rem; padding-left: 2rem; padding-right: 2rem; }
    [data-testid="metric-container"] {
        background: #f8f8f8;
        border: 1px solid #e8e8e8;
        border-radius: 12px;
        padding: 16px 20px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] { border-radius: 8px 8px 0 0; padding: 8px 20px; font-weight: 500; }
    .stButton > button { border-radius: 8px; font-weight: 500; }
    hr { border: none; border-top: 1px solid #e8e8e8; margin: 0.8rem 0; }
</style>
""", unsafe_allow_html=True)


def main():
    if not check_password():
        st.stop()

    with st.sidebar:
        st.markdown("## 🔴 Hodemeier Hub")
        st.markdown("---")
        pages = {
            "📊  ApoRed Predictor": "predictor",
            "📧  Email Generator": "email",      # ← NEU
            "🔐  Account Manager": "google",
        }
        choice_label = st.radio("Nav", list(pages.keys()), label_visibility="collapsed")
        choice = pages[choice_label]
        st.markdown("---")
        st.markdown("<p style='font-size:12px;color:#555;'>Admin</p>", unsafe_allow_html=True)
        if st.button("⏻  Logout", use_container_width=True):
            st.session_state["authenticated"] = False
            st.rerun()
            
    if choice == "predictor":
        render_predictor_tab()
    elif choice == "email":                    # ← NEU
        render_email_generator_tab()
    elif choice == "google":
        render_automation_tab()

if __name__ == "__main__":
    main()
