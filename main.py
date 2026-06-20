# AI Real-Time Gym Coach this is the main file for the streamlit app. It will import the necessary libraries and set up the page configuration. It will also display the title and a brief description of the app.
import streamlit as st
from services.auth.login_wall import render_login_wall

def main():
    st.set_page_config(
        page_icon="🏋️‍♂️",
        page_title="⛹️AI Real-Time Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    if not render_login_wall():
        return  # Stop further execution if the user is not logged in
    st.write("hello")
if __name__ == "__main__":
    main()