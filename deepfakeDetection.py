import streamlit as st
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

def process_audio_file(uploaded_file):
    st.audio(uploaded_file, format='audio/wav')

    st.write("### Waveform of Uploaded Audio:")
    with sf.SoundFile(uploaded_file) as audio_file:
        audio_data = audio_file.read()
        num_samples = len(audio_data)
        duration = num_samples / audio_file.samplerate

        time = np.linspace(0, duration, num_samples)
        plt.figure(figsize=(10, 4))
        plt.plot(time, audio_data)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        st.pyplot()

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
