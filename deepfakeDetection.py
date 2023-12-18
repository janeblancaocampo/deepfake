import streamlit as st
import io
import matplotlib.pyplot as plt
from pydub import AudioSegment
import numpy as np

def process_audio_file(uploaded_file):
    st.audio(uploaded_file, format='audio/wav')

    st.write("### Waveform of Uploaded Audio:")
    audio_data = io.BytesIO(uploaded_file.read())
    audio = AudioSegment.from_file(audio_data)
    samples = np.array(audio.get_array_of_samples())

    plt.figure(figsize=(10, 4))
    plt.plot(samples)
    plt.xlabel('Sample')
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
