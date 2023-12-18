import streamlit as st
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def process_audio_file(uploaded_file):
    st.write("Generating waveform...")

    # Load audio file
    audio_data, _ = librosa.load(uploaded_file, sr=None)

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio_data, sr=44100)  # Adjust 'sr' according to your audio file's sample rate
    plt.title('Audio Waveform')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    st.pyplot()

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
