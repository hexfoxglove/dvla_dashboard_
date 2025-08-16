# main.py
import streamlit as st
from auth import login, signup

# Placeholder role mapping (later move to Firestore)
USER_ROLES = {
    "admin@dvla.com": "admin",
    "test@user.com": "customer"
}

# Session state init
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None

st.sidebar.title("DVLA Dashboard")

if st.session_state.user:
    st.sidebar.success(f"Logged in as {st.session_state.user}")
    if st.session_state.role == "admin":
        st.sidebar.write("Role: DVLA Admin")
        import dvla_admin_portal
        dvla_admin_portal.show()
    else:
        st.sidebar.write("Role: Customer")
        import customer_portal
        customer_portal.show()

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.role = None
        st.experimental_rerun()
else:
    choice = st.sidebar.radio("Login/Signup", ["Login", "Signup"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Signup":
        if st.button("Signup"):
            result = signup(email, password)
            if result:
                st.success("Account created! Please login.")
    else:
        if st.button("Login"):
            result = login(email, password)
            if result:
                st.session_state.user = email
                st.session_state.role = USER_ROLES.get(email, "customer")
                st.experimental_rerun()

