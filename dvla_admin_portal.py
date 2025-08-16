import streamlit as st

def show():
    st.title("🛠️ DVLA Agent Dashboard")
    st.write("Welcome DVLA Agent! Manage customer requests and feedback here.")

    menu = st.sidebar.radio("Menu", ["Requests", "Cars", "Feedback"])

    if menu == "Requests":
        st.subheader("All Service Requests")
        requests = st.session_state.get("requests", [])
        if requests:
            for req in requests:
                st.write(f"- {req['car']} | {req['type']} | Status: {req['status']}")
        else:
            st.info("No requests yet.")

    elif menu == "Cars":
        st.subheader("All Registered Cars")
        cars = st.session_state.get("cars", [])
        if cars:
            for car in cars:
                st.write(f"- {car['plate']} ({car['model']}, {car['year']})")
        else:
            st.info("No cars registered yet.")

    elif menu == "Feedback":
        st.subheader("All Customer Feedback")
        feedback = st.session_state.get("feedback", [])
        if feedback:
            for fb in feedback:
                st.write(f"- {fb['message']}")
        else:
            st.info("No feedback yet.")
