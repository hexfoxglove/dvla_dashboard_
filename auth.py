# auth.py
import requests

# Your Firebase Web API Key (from firebaseConfig)
API_KEY = "AIzaSyAjUuxnIuFwaxpbR8mwNS2tottqnWI-w1A"

# Base URLs for Firebase Identity Toolkit REST API
SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
USERINFO_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={API_KEY}"

def signup(email: str, password: str):
    """
    Create a new Firebase Auth user with email + password.
    Returns dict with idToken, refreshToken, localId if successful.
    """
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(SIGNUP_URL, json=payload)
    return response.json()

def login(email: str, password: str):
    """
    Log in existing Firebase Auth user.
    Returns dict with idToken, refreshToken, localId if successful.
    """
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(LOGIN_URL, json=payload)
    return response.json()

def get_user_info(id_token: str):
    """
    Fetch user profile info using their ID token.
    Useful after login to confirm email, uid, etc.
    """
    payload = {
        "idToken": id_token
    }
    response = requests.post(USERINFO_URL, json=payload)
    return response.json()

