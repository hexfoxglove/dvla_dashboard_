import firebase_admin
from firebase_admin import credentials, firestore
import json
import streamlit as st

def get_db():
    if not firebase_admin._apps:
        sa = json.loads(st.secrets["FIREBASE_SERVICE_ACCOUNT"])
        cred = credentials.Certificate(sa)
        firebase_admin.initialize_app(cred)
    return firestore.client()

# convenient global
db = get_db()
