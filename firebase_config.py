# firebase_config.py
import firebase_admin
from firebase_admin import credentials, auth

# Load service account key (downloaded from Firebase Console)
cred = credentials.Certificate("firebase_secret.json")
firebase_admin.initialize_app(cred)

