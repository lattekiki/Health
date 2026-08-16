import json
import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Ethiopian Healthcare Companion",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom styling for a clean medical theme
st.markdown(
    """
    <style>
        .main { background-color: #f8f9fa; }
        .sidebar .sidebar-content { background-color: #ffffff; }
        h1, h2, h3 { color: #1b4332; }
        .stButton>button { background-color: #2d6a4f; color: white; border-radius: 6px; }
        .stButton>button:hover { background-color: #40916c; color: white; }
    </style>
""",
    unsafe_allow_html=True,
)


# Load JSON translation files
@st.cache_data
def load_translations():
    with open("eng.json", "r", encoding="utf-8") as f:
        eng = json.load(f)
    with open("amh.json", "r", encoding="utf-8") as f:
        amh = json.load(f)
    return {"English": eng, "አማርኛ": amh}


translations = load_translations()

# Initialize session state for language selection
if "lang" not in st.session_state:
    st.session_state.lang = "English"

# Import module pages
import ANC
import Chronic
import Input
import Medication_reminder
import PostOP

# --- SIDEBAR LANGUAGE TOGGLE & NAVIGATION ---
st.sidebar.markdown("### 🌐 Localization / ቋንቋ")
selected_lang = st.sidebar.selectbox(
    "Choose Language",
    ["English", "አማርኛ"],
    index=0 if st.session_state.lang == "English" else 1,
)
st.session_state.lang = selected_lang

# Get active dictionary based on selection
t = translations[st.session_state.lang]

st.sidebar.title("🏥 Health Manager")
st.sidebar.markdown("---")

menu_selection = st.sidebar.radio(
    "Navigation Menu",
    [
        "Medication Reminder",
        "ANC (Antenatal Care)",
        "Chronic Illness",
        "PostOP Care",
        "Data Input",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**System Status:** Online \n\n*Integrated with local health tracking guidelines.*"
)

# Map menu selections to their corresponding modules
modules = {
    "Medication Reminder": Medication_reminder,
    "ANC (Antenatal Care)": ANC,
    "Chronic Illness": Chronic,
    "PostOP Care": PostOP,
    "Data Input": Input,
}

active_module = modules.get(menu_selection)

# Route safely: tries to pass 't', falls back if the module page hasn't been updated yet
# Route safely
if active_module:
    active_module.render_page(t)