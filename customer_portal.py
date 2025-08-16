

import streamlit as st

def show():
    st.title("🚗 Customer Dashboard")
    st.write("Welcome! Manage your car and service requests here.")

    menu = st.sidebar.radio("Menu", ["My Cars", "Service Requests", "Feedback"])

    # --- My Cars ---
    if menu == "My Cars":
        st.subheader("My Cars")

        if "cars" not in st.session_state:
            st.session_state.cars = []

        with st.form("car_form"):
            plate = st.text_input("Car Plate Number")
            model = st.text_input("Car Model")
            year = st.number_input("Year", min_value=1980, max_value=2030, step=1)
            submitted = st.form_submit_button("Add Car")

            if submitted:
                st.session_state.cars.append({"plate": plate, "model": model, "year": year})
                st.success(f"Car {plate} added!")

        if st.session_state.cars:
            st.write("### Registered Cars")
            for car in st.session_state.cars:
                st.write(f"- {car['plate']} ({car['model']}, {car['year']})")

    # --- Service Requests ---
    elif menu == "Service Requests":
        st.subheader("Service Requests")

        if "requests" not in st.session_state:
            st.session_state.requests = []

        with st.form("service_form"):
            car_plate = st.selectbox(
                "Select Car",
                [car["plate"] for car in st.session_state.get("cars", [])] or ["No Cars Added"]
            )
            service_type = st.selectbox("Service Type", ["Renewal", "Repair", "License Update"])
            details = st.text_area("Additional Details")
            submitted = st.form_submit_button("Submit Request")

            if submitted and car_plate != "No Cars Added":
                st.session_state.requests.append(
                    {"car": car_plate, "type": service_type, "details": details, "status": "Pending"}
                )
                st.success("Request submitted successfully!")

        if st.session_state.requests:
            st.write("### My Requests")
            for req in st.session_state.requests:
                st.write(f"- {req['car']} | {req['type']} | Status: {req['status']}")

    # --- Feedback ---
    elif menu == "Feedback":
        st.subheader("Feedback & Issues")

        if "feedback" not in st.session_state:
            st.session_state.feedback = []

        with st.form("feedback_form"):
            message = st.text_area("Your Feedback or Problem")
            submitted = st.form_submit_button("Submit Feedback")
            if submitted:
                st.session_state.feedback.append({"message": message})
                st.success("Thank you for your feedback!")

        if st.session_state.feedback:
            st.write("### Previous Feedback")
            for fb in st.session_state.feedback:
                st.write(f"- {fb['message']}")
