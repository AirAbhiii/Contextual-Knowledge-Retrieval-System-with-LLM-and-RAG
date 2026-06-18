"""
Home page for Streamlit authentication interface.
"""

import logging

import streamlit as st

from utils.api_client import create_user, login_user, get_api_token

# Hide sidebar for cleaner look
hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="LangGraph Chat - Login")

st.title("🔐 Welcome to LangGraph Assistant")

token = ""

# Step 1: Initialize session_id
if "session_id" not in st.session_state:
    st.session_state["session_id"] = "default_user_session"

# Step 2: Render simplified form
with st.form("auth_form"):
    username = st.text_input("Enter your name to start")
    submit = st.form_submit_button("Start Chatting")

# Step 3: Handle redirection
if submit:
    if not username:
        st.error("Name is required.")
    else:
        st.session_state["username"] = username
        st.switch_page("pages/Chat.py")

# Debug logs section
with st.expander("📜 Debug Logs"):
    try:
        with open("app.log", "r") as log_file:
            st.text(log_file.read())
    except FileNotFoundError:
        st.warning("Log file not found yet.")
