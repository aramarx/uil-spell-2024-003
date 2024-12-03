import streamlit as st

# Hardcoded list of users (for demonstration purposes)
USERS = {
    "user1": "pass12345",
    "user2": "pass54321",
}

def login():
    """Function to handle user login"""
    st.title("Login Page")
    
    # If the user is already logged in, don't show the login form
    if "username" in st.session_state:
        st.success(f"Welcome, {st.session_state['username']}!")
        return True

    # Display login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Simple authentication logic
        if username in USERS and USERS[username] == password:
            st.session_state["username"] = username
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Rerun the app to load the main app after login
            return True
        else:
            st.error("Invalid username or password")
    
    return False

def main_app():
    """Main application after login"""
    st.title("Main Application")
    
    # Your main application logic here
    st.write("Visit the main application at [https://spulflaskt05df.vercel.app](https://spulflaskt05df.vercel.app)")
    #st.write("You are logged in and can now use the app.")
    if st.button("Log out"):
        st.session_state.clear()  # Clear session state on logout
        st.experimental_rerun()  # Rerun to go back to login page

def main():
    """Main function to switch between login page and main app"""
    # Check if user is logged in
    if not login():
        main_app()  # Show the main app if logged in
    else:
        pass

if __name__ == "__main__":
    main()
