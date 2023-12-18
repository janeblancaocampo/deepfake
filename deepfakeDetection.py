import streamlit as st
from pydub import AudioSegment

def is_within_6_seconds(audio_file):
    audio = AudioSegment.from_file(audio_file)
    duration = len(audio) / 1000  # Duration in seconds
    return duration <= 6

def main():
    st.title('Audio File Duration Checker')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if is_within_6_seconds(uploaded_file):
            st.success("The audio file is within 6 seconds.")
        else:
            st.error("The audio file exceeds 6 seconds.")

if __name__ == "__main__":
    main()
