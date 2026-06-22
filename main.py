# AI Real-Time Gym Coach this is the main file for the streamlit app. It will import the necessary libraries and set up the page configuration. It will also display the title and a brief description of the app.
import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_default import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS 
def main():
    st.set_page_config(
        page_icon="🏋️‍♂️",
        page_title="⛹️AI Real-Time Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    if not render_login_wall():
        return  # Stop further execution if the user is not logged in
    initial_session_defaults()
    workout_started = st.session_state.get("workout_started", False)
    with st.sidebar:
       st.title("⛹️ AS AI Coach")

       if st.session_state.username:
        st.caption(f"👤 Login as, {st.session_state.username}!")

        st.divider()

        st.subheader("📋 Workout Plan")

        if not workout_started:
            st.selectbox("Exercise",options=EXERCISE_OPTIONS,key="plan_exercise")
            st.number_input("Sets",min_value=0,max_value=50,key="plan_sets",step=1)
            st.number_input("Reps per Set",min_value=0,max_value=50,key="plan_reps")

            st.markdown("")
            start_session_button= st.button("Start Workout",width="stretch",key="start_session_button")
            if start_session_button:
               st.session_state["workout_started"] = True
                 # Rerun the app to update the session state and proceed to the main content
            else:
               st.write("workout started:")
    main()