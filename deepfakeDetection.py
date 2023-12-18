import streamlit as st
import librosa.display
import matplotlib.pyplot as plt
from pydub import AudioSegment
import io

def process_audio_file(uploaded_file):
    st.write("Generating waveform...")

    # Convert the uploaded file to WAV format
    audio_bytes = uploaded_file.getvalue()
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    wav_file = io.BytesIO()
    audio.export(wav_file, format="wav")
    wav_file.seek(0)

    # Load the converted WAV file
    audio_data, _ = librosa.load(wav_file, sr=None)

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
