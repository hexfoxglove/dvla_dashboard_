import streamlit as st
from customer_portal import show as customer_dashboard
from dvla_admin_portal import show as dvla_dashboard

# --- Initialize session state ---
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None
if "accounts" not in st.session_state:
    st.session_state.accounts = {
        "customer": {"password": "1234", "role": "customer"},
        "agent": {"password": "4321", "role": "agent"},
    }
if "invite_codes" not in st.session_state:
    # Pre-generated codes for agent signup
    st.session_state.invite_codes = ["AGENT2025", "DVLAAGENT1"]

# --- Login page ---
def login():
    st.title("🔑 DVLA Dashboard")
    choice = st.radio("Choose Action:", ["Login", "Sign Up"])

    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in st.session_state.accounts:
                if st.session_state.accounts[username]["password"] == password:
                    st.session_state.user = username
                    st.session_state.role = st.session_state.accounts[username]["role"]
                    st.rerun()
                else:
                    st.error("Incorrect password.")
            else:
                st.error("Account does not exist. Please sign up.")

    elif choice == "Sign Up":
        st.subheader("Sign Up")
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type="password")
        role = st.radio("Role:", ["Customer", "DVLA Agent"])

        if st.button("Sign Up"):
            if username in st.session_state.accounts:
                st.error("Username already exists.")
            elif not username or not password:
                st.error("Please enter both username and password.")
            else:
                # Agent signup requires invite code
                if role == "DVLA Agent":
                    invite = st.text_input("Enter Agent Invite Code")
                    if invite not in st.session_state.invite_codes:
                        st.error("Invalid or missing invite code. Ask admin for a valid code.")
                        return
                    else:
                        # consume invite code
                        st.session_state.invite_codes.remove(invite)

                st.session_state.accounts[username] = {
                    "password": password,
                    "role": "customer" if role == "Customer" else "agent"
                }
                st.success("Account created successfully!")
                if role == "Customer":
                    st.info("Now switch to 'Login' above to access your account.")
                else:
                    st.info("Agent account created. Please log in with your credentials.")



# --- Logout ---
def logout():
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.role = None
        st.rerun()

# --- Main app routing ---
if st.session_state.user:
    logout()  # show logout button in sidebar
    if st.session_state.role == "customer":
        customer_dashboard()
    elif st.session_state.role == "agent":
        dvla_dashboard()
else:
    login()
