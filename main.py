# main.py
import streamlit as st
from auth import login, signup

st.title("DVLA Dashboard 🚗")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Sign Up":
    st.subheader("Create New Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        result = signup(email, password)
        if "error" in result:
            st.error(result["error"]["message"])
        else:
            st.success("Account created successfully!")

elif choice == "Login":
    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login(email, password)
        if "error" in result:
            st.error(result["error"]["message"])
        else:
            st.success("Login successful!")
            st.write("User Info:", result)
