import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()

st.title("Welcome to Cheatham Speller β")

st.write("🔒 Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "uiltest" and password == "cheathamtest":
        st.session_state.logged_in = True
        st.success("✔️Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/page1.py")
    else:
        st.error("❌Incorrect username or password")
