import streamlit as st

# Import der Unterseiten aus den entsprechenden Modulen
# Wichtig: In predictor.py muss eine Funktion 'run_predictor()' existieren.
# Wichtig: In automation.py muss eine Funktion 'run_dashboard()' existieren.
from apored_predictor.predictor import run_predictor
from email_manager.automation import run_dashboard

# Konfiguration der Seite
st.set_page_config(
    page_title="Finn's IT-Hub",
    page_icon="🖥️",
    layout="wide"
)

def main():
    # Sidebar für die Navigation zwischen den Projekten
    st.sidebar.title("🚀 Projekt-Hub")
    st.sidebar.write("Willkommen, Finn!")
    st.sidebar.markdown("---")
    
    # Auswahlmenü
    selection = st.sidebar.radio(
        "Wähle ein Projekt:",
        ["Fortnite Win Predictor", "Email Dashboard"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("IT-Lehrling Projekt @ TBZ")

    # Logik zum Laden der entsprechenden Seite
    if selection == "Fortnite Win Predictor":
        run_predictor()
    elif selection == "Email Dashboard":
        run_dashboard()

if __name__ == "__main__":
    main()
