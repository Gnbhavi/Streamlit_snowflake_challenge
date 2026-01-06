import streamlit as st
import importlib.util
import pathlib

st.sidebar.title("30 Days of AI")
day_folders = sorted([f for f in pathlib.Path().iterdir() if f.is_dir() and f.name.startswith("Day")])
day_choice = st.sidebar.selectbox("Choose a day", [folder.name for folder in day_folders])

# Journal in sidebar
notes_path = pathlib.Path(day_choice) / "notes.md"
st.sidebar.subheader("📓 Journal")
if notes_path.exists():
    st.sidebar.markdown(notes_path.read_text())
else:
    st.sidebar.info("No journal yet for this day.")

# Main area: run the first .py file inside the folder
st.title(f"{day_choice} Showcase")
py_files = list(pathlib.Path(day_choice).glob("*.py"))
if py_files:
    file_path = py_files[0]  # pick the first .py file
    spec = importlib.util.spec_from_file_location("day_app", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
else:
    st.error(f"No .py file found in {day_choice}")

# st.sidebar.markdown(
#     """
#     <hr style="margin-top:50px; margin-bottom:10px;">
#     <div style="text-align:center">
#         Made with ❤️ during my 30‑Day AI Challenge <br>
#         <a href="https://github.com/Gnbhavi" target="_blank">🌐 GitHub</a> |
#         <a href="https://www.linkedin.com/in/bhavithran" target="_blank">🔗 LinkedIn</a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

st.sidebar.markdown(
    """
    <hr style="margin-top:50px; margin-bottom:10px;">
    <div style="text-align:center; font-size: 14px;">
        Made with ❤️ during my 30‑Day AI Challenge <br>
        <a href="https://github.com/Gnbhavi" target="_blank" style="text-decoration:none; color:#00FFFF;">🌐 GitHub</a> |
        <a href="https://www.linkedin.com/in/bhavithran" target="_blank" style="text-decoration:none; color:#39FF14;">🔗 LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)