import streamlit as st
import os

# Access credentials from st.secrets for Streamlit Cloud or Vercel (if available)
try:
    USER_CREDENTIALS = {
        "user5a": st.secrets["user5a"],
        "user5b": st.secrets["user5b"],
        "user5c": st.secrets["user5c"],
        "user5t": st.secrets["user5t"],
        "user6a": st.secrets["user6a"],
        "user6b": st.secrets["user6b"],
        "user6c": st.secrets["user6c"],
        "user6t": st.secrets["user6t"]
    }
except KeyError as e:
    st.error(f"Error: {e}. Please check your secrets configuration.")
    st.stop()  # Stop the app execution if secrets are not found

def login():
    """Function to handle user login"""
    st.title("Login Page")
    
    # If the user is already logged in, don't show the login form
    if "username" in st.session_state:
        st.success(f"Welcome, {st.session_state['username']}!")
        # Redirect to the Vercel URL after successful login
        st.experimental_rerun()  # Rerun to load the main app
        st.experimental_redirect("https://spulflaskt05df.vercel.app")
        return True

    # Display login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Authentication logic: Check if username and password are correct
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            # Store username in session state
            st.session_state["username"] = username
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Rerun the app to load the main app after login
            return True
        else:
            st.error("Invalid username or password")
    
    return False

def main_app():
    """Main application to show after successful login"""
    st.title("Main Application")
    st.write("You are now logged in and can interact with the main app!")
    if st.button("Log out"):
        st.session_state.clear()  # Clear session state on logout
        st.experimental_rerun()  # Rerun to go back to login page

def main():
    """Main function to handle page logic"""
    if not login():
        main_app()  # Show the main app if logged in
    else:
        pass

if __name__ == "__main__":
    main()
