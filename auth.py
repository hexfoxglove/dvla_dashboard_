import json
import streamlit as st
import pyrebase
from firebase_admin import auth as admin_auth
from firebase_config import db

# ---------- Pyrebase init (client-side Auth) ----------
def _get_pyrebase():
    cfg = json.loads(st.secrets["FIREBASE_WEB_CONFIG"])
    return pyrebase.initialize_app(cfg)

def _auth_client():
    return _get_pyrebase().auth()

# ---------- Firestore: user profile ----------
def _users_coll():
    return db.collection("users")

def ensure_user_profile(uid: str, email: str, default_role: str = "customer"):
    doc_ref = _users_coll().document(uid)
    doc = doc_ref.get()
    if not doc.exists:
        doc_ref.set({
            "email": email,
            "role": default_role,
            "created_at": db.FIELD_SERVER_TIMESTAMP if hasattr(db, "FIELD_SERVER_TIMESTAMP") else None,
        })

def get_user_profile(uid: str):
    doc = _users_coll().document(uid).get()
    return doc.to_dict() if doc.exists else None

def set_user_role(uid: str, role: str):
    _users_coll().document(uid).set({"role": role}, merge=True)

# ---------- Signup / Login ----------
def signup_email_password(email: str, password: str):
    auth = _auth_client()
    user = auth.create_user_with_email_and_password(email, password)
    # Refresh to get idToken
    user = auth.refresh(user["refreshToken"])
    id_token = user["idToken"]

    # Verify token using Admin SDK to get UID
    decoded = admin_auth.verify_id_token(id_token)
    uid = decoded["uid"]

    ensure_user_profile(uid, email, default_role="customer")
    profile = get_user_profile(uid)
    return {"uid": uid, "email": email, "idToken": id_token, "profile": profile}

def login_email_password(email: str, password: str):
    auth = _auth_client()
    user = auth.sign_in_with_email_and_password(email, password)
    # Refresh to get a fresh idToken
    user = auth.refresh(user["refreshToken"])
    id_token = user["idToken"]

    decoded = admin_auth.verify_id_token(id_token)
    uid = decoded["uid"]
    profile = get_user_profile(uid)
    # If no profile (e.g., created outside app), create one
    if not profile:
        ensure_user_profile(uid, email, default_role="customer")
        profile = get_user_profile(uid)

    return {"uid": uid, "email": email, "idToken": id_token, "profile": profile}

# ---------- Session helpers ----------
SESSION_KEY = "auth_state"

def get_session():
    if SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = {
            "authenticated": False,
            "uid": None,
            "email": None,
            "idToken": None,
            "role": None
        }
    return st.session_state[SESSION_KEY]

def set_session(auth_blob: dict):
    s = get_session()
    s["authenticated"] = True
    s["uid"] = auth_blob.get("uid")
    s["email"] = auth_blob.get("email")
    s["idToken"] = auth_blob.get("idToken")
    s["role"] = (auth_blob.get("profile") or {}).get("role", "customer")

def logout():
    if SESSION_KEY in st.session_state:
        st.session_state.pop(SESSION_KEY, None)

def guard_role(required: str) -> bool:
    s = get_session()
    return s.get("authenticated") and s.get("role") == required
