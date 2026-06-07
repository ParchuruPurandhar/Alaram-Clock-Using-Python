import streamlit as st
import datetime
import time

st.title("⏰ Alarm Clock")

# Time input
alarm_time = st.time_input("Select Alarm Time")

if st.button("Set Alarm"):

    st.success(f"Alarm set for {alarm_time}")

    placeholder = st.empty()

    while True:
        current_time = datetime.datetime.now().time()

        placeholder.write(
            f"Current Time: {current_time.strftime('%H:%M:%S')}"
        )

        if (
            current_time.hour == alarm_time.hour
            and current_time.minute == alarm_time.minute
        ):
            st.warning("🔔 Alarm Time Reached!")
            st.balloons()

            # Play alarm sound in browser
            audio_file = open("alarm.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

            break

        time.sleep(1)
