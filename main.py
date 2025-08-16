import streamlit as st

def main():
    st.title("DVLA Spintex Dashboard")
    st.write("Welcome to the DVLA Dashboard Prototype 🚗")

    menu = ["Home", "Customer Dashboard", "DVLA Dashboard"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        st.subheader("Home Page")
        st.write("This is the starting point. Use the sidebar to navigate.")
    elif choice == "Customer Dashboard":
        st.subheader("Customer Dashboard")
        st.write("Customer features will appear here.")
    elif choice == "DVLA Dashboard":
        st.subheader("DVLA Dashboard")
        st.write("DVLA staff features will appear here.")

if __name__ == "__main__":
    main()
