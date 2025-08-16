# auth.py
import requests

# Your Firebase Web API Key (from firebaseConfig)
import streamlit as st

API_KEY = st.secrets["firebase"]["apiKey"]

# Firebase endpoints
SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

def signup(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(SIGNUP_URL, data=payload)
    if response.status_code == 200:
        return response.json()  # contains idToken, refreshToken, etc.
    else:
        st.error(response.json().get("error", {}).get("message", "Signup failed"))
        return None

def login(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(LOGIN_URL, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(response.json().get("error", {}).get("message", "Login failed"))
        return None
