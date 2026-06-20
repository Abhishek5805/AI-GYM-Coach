import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True  # User is already logged in
    st.title("⛹️AI Real-Time Gym Trainer")
    st.markdown("### Welcome ! Please enter a username to start")

    with st.form("login_form",clear_on_submit=False):
        username = st.text_input("Name (unique)",placeholder="Enter your name e.g. Abhishek")
        submit_button = st.form_submit_button("Start session",width="stretch")
    
    if submit_button:
        if not username:
            st.error("Name cannot be empty. Please enter a valid name.")
            return False
        st.session_state["username"] = username
        st.session_state["user_id"] = "1" # Using username as user_id for simplicity

        st.rerun()  # Rerun the app to update the session state and proceed to the main content
    return False 