import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import json

if not firebase_admin._apps:
    firebase_config = json.loads(st.secrets["FIREBASE_SERVICE_ACCOUNT"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

