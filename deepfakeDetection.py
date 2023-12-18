import streamlit as st
import sounddevice as sd
import numpy as np
import io
from scipy.io.wavfile import write as write_wav

def record_audio(duration=6, fs=44100):
    st.subheader("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    st.subheader("Recording ended.")
    return recording

def main():
    st.title('Audio File Uploader & Recorder')

    option = st.radio("Choose an option:", ("Upload Audio File", "Record Audio"))

    if option == "Upload Audio File":
        uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
        if uploaded_file is not None:
            st.audio(uploaded_file, format='audio/wav')

    elif option == "Record Audio":
        duration = st.slider("Recording duration (seconds):", min_value=1, max_value=10, value=6)
        record_button = st.button("Start Recording")

        if record_button:
            recording = record_audio(duration)
            st.audio(io.BytesIO(recording), format='audio/wav')

if __name__ == "__main__":
    main()
