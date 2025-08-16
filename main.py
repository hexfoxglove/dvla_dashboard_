# main.py
# main.py
import streamlit as st
from auth import login, signup

st.set_page_config(page_title="DVLA Dashboard", layout="centered")

st.title("DVLA Dashboard")

# Page switcher
page = st.sidebar.selectbox("Choose Page", ["Login", "Signup"])

if page == "Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login(email, password)
        if user:
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials. Try again.")

elif page == "Signup":
    st.subheader("Create an Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        user = signup(email, password)
        if user:
            st.success("Account created successfully! You can now log in.")
        else:
            st.error("Signup failed. Try again.")

