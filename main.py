# AI Real-Time Gym Coach this is the main file for the streamlit app. It will import the necessary libraries and set up the page configuration. It will also display the title and a brief description of the app.
import streamlit as st
import os
from services.auth.login_wall import render_login_wall
from services.state.session_default import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import load_css, inject_local_font
from services.persistence.exercise_repository import init_db
def main():
    st.set_page_config(
        page_icon="🏋️‍♂️",
        page_title="⛹️AI Real-Time Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    load_css(os.path.join(os.getcwd(), "static", "style.css"))
    inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")

    init_db()  # Initialize the database and create tables if they don't exist
    
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
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")

            st.info(f"**{exercise}** - {sets} sets of {reps} reps")

            end_session_button = st.button("End Workout", key="end_session_button",width="stretch")
            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()  # Rerun the app to reset the session state and return to the workout plan selection
        if workout_started:
            st.divider() 

            exercise = st.session_state.get("plan_exercise")
            total_reps= st.session_state.get("reps")
            current_set_reps= st.session_state.get("current_set_reps")
            reps_per_set= st.session_state.get("plan_reps")
            sets_completed= st.session_state.get("sets_completed")
            target_sets= st.session_state.get("plan_sets")

            st.subheader("progress")

            st.metric("Total Reps", f"{total_reps} ")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.knee_angle}°")
                st.metric("Back Angle", f"{st.session_state.back_angle}°")
                st.metric("Depth Status", st.session_state.depth_status)

            elif exercise == "Push-ups":
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Body Alignment", st.session_state.body_alignment)
                st.metric("Hip Position", st.session_state.hip_status)

            elif exercise == "Biceps Curls (Dumbbell)":
                st.subheader("Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Shoulder Stability", st.session_state.shoulder_status)
                st.metric("Swing Detection", st.session_state.swing_status)

            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Arm Extension", st.session_state.extension_status)
                st.metric("Back Arch", st.session_state.back_arch_status)

            elif exercise == "Lunges":
                st.subheader("Lunge Metrics")
                st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}°")
                st.metric("Torso Angle", f"{st.session_state.torso_angle}°")
                st.metric("Balance Status", st.session_state.balance_status)






main()