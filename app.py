import streamlit as st
import datetime
import time

st.set_page_config(page_title="Digital Alarm Clock", page_icon="⏰")

st.title("⏰ Digital Alarm Clock")

# Alarm Time Input
alarm_time = st.time_input("Set Alarm Time")

# Placeholder for Digital Clock
clock_placeholder = st.empty()

# Session State
if "alarm_set" not in st.session_state:
    st.session_state.alarm_set = False

if st.button("Set Alarm"):
    st.session_state.alarm_set = True
    st.success(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")

# Live Clock
while True:
    current_time = datetime.datetime.now()

    clock_placeholder.markdown(
        f"""
        <h1 style='text-align:center;'>
        {current_time.strftime('%H:%M:%S')}
        </h1>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.alarm_set:
        if (
            current_time.hour == alarm_time.hour
            and current_time.minute == alarm_time.minute
            and current_time.second == 0
        ):
            st.warning("🔔 Alarm Time Reached!")
            st.balloons()

            # Play sound file
            with open("alarm.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()

            st.audio(audio_bytes, format="audio/mp3")
            st.session_state.alarm_set = False

    time.sleep(1)
