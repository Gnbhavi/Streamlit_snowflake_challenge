import streamlit as st
from datetime import datetime
from snowflake.snowpark import Session

# --- Page Config ---
st.set_page_config(
    page_title="Portfolio Manager",
    page_icon="📊",
    layout="wide"
)

# --- Sidebar with Date ---
st.sidebar.title("📅 Date")
today = datetime.now().strftime("%A, %d %B %Y")
st.sidebar.info(today)

# --- Main Title & Subtitle ---
st.title("📈 Portfolio Manager")
st.subheader("30 Days of AI, Streamlit and Snowflake")

# --- Connect to Snowflake ---
session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Quick test query
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]
st.success(f"Connected to Snowflake! Version: {version}")

# --- Query your investments table ---
df = session.table("investments").to_pandas()
st.dataframe(df, use_container_width=True)

# --- Footer with GitHub link ---
st.markdown(
    """
    <hr style="margin-top:50px; margin-bottom:10px;">
    <div style="text-align:center">
        Made with ❤️ using Streamlit & Snowflake <br>
        <a href="https://github.com/Gnbhavi" target="_blank">🌐 Gn Bhavi</a>
    </div>
    """,
    unsafe_allow_html=True
)