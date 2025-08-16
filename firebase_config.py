import firebase_admin
from firebase_admin import credentials, firestore

SERVICE_ACCOUNT_FILE = "serviceAccount.json"

cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
firebase_admin.initialize_app(cred)

db = firestore.client()
