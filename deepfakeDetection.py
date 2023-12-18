import streamlit as st
from pydub import AudioSegment
import io

def main():
    st.title("Audio Player App")
    st.write("Upload an audio file and click play to listen!")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/wav')

if __name__ == "__main__":
    main()
