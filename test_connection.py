from firebase_config import db

def test_firestore():
    doc_ref = db.collection("test_collection").document("test_doc")
    doc_ref.set({"message": "Hello from GitHub -> Colab -> Firebase"})
    doc = doc_ref.get()
    print("Firestore says:", doc.to_dict())

if __name__ == "__main__":
    test_firestore()
