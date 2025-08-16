import streamlit as st
from auth import (
    signup_email_password, login_email_password,
    get_session, set_session, logout, guard_role
)

st.set_page_config(page_title="DVLA Dashboard", page_icon="🚗", layout="centered")

# --------- Placeholder dashboards ---------
def customer_dashboard():
    st.header("Customer Dashboard")
    st.write("Welcome! Add/view cars, create service requests, track status… (coming next)")

def dvla_dashboard():
    st.header("DVLA Admin Dashboard")
    st.write("View/update customer records, approve statuses… (coming next)")

# --------- UI helpers ---------
def show_auth_forms():
    tab_login, tab_signup = st.tabs(["Login", "Sign up"])

    with tab_login:
        st.subheader("Login")
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
        if submitted:
            try:
                auth_blob = login_email_password(email, password)
                set_session(auth_blob)
                st.success("Logged in successfully.")
                st.rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

    with tab_signup:
        st.subheader("Sign up")
        with st.form("signup_form", clear_on_submit=False):
            email = st.text_input("Email", key="su_email")
            password = st.text_input("Password", type="password", key="su_pass")
            submitted = st.form_submit_button("Create account")
        if submitted:
            try:
                auth_blob = signup_email_password(email, password)
                set_session(auth_blob)
                st.success("Account created and logged in.")
                st.rerun()
            except Exception as e:
                st.error(f"Signup failed: {e}")

def show_topbar():
    s = get_session()
    cols = st.columns([1,1,1,1,1])
    with cols[-1]:
        if s.get("authenticated"):
            if st.button("Log out"):
                logout()
                st.rerun()

# --------- Router ---------
def router():
    s = get_session()
    st.title("DVLA Dashboard")

    show_topbar()

    if not s["authenticated"]:
        show_auth_forms()
        return

    # Authenticated → route by role
    role = s.get("role", "customer")
    if role == "dvla":
        dvla_dashboard()
    else:
        customer_dashboard()

if __name__ == "__main__":
    router()
