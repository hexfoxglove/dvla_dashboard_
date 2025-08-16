import streamlit as st
from customer_portal import show as customer_dashboard
from dvla_admin_portal import show as dvla_dashboard

# --- Initialize session state ---
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None

# --- Login page ---
def login():
    st.title("🔑 DVLA Dashboard Login")

    role = st.radio("Login as:", ["Customer", "DVLA Agent"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:  # ✅ Simple dummy login check
            st.session_state.user = username
            st.session_state.role = "customer" if role == "Customer" else "agent"
            st.rerun()  # rerun only AFTER successful login
        else:
            st.error("Please enter both username and password.")

# --- Logout ---
def logout():
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.role = None
        st.rerun()  # rerun only AFTER logout

# --- Main app routing ---
if st.session_state.user:
    logout()
    if st.session_state.role == "customer":
        customer_dashboard()
    elif st.session_state.role == "agent":
        dvla_dashboard()
else:
    login()

