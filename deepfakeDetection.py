import streamlit as st
from pydub import AudioSegment
import librosa.display
import io

def process_audio_file(uploaded_file):
    st.audio(uploaded_file, format='audio/wav')

    audio_bytes = io.BytesIO(uploaded_file.read())
    audio = AudioSegment.from_file(audio_bytes)

    # Convert to WAV format
    with io.BytesIO() as wav_buffer:
        audio.export(wav_buffer, format="wav")
        wav_buffer.seek(0)

        # Load audio using librosa
        y, sr = librosa.load(wav_buffer)

        # Plot waveform
        plt.figure(figsize=(8, 4))
        plt.title('Waveform Visualization')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        librosa.display.waveshow(y, sr=sr)
        st.pyplot()

def main():
    st.title('Audio File Uploader and Waveform Visualizer')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Audio'):
            process_audio_file(uploaded_file)

if __name__ == "__main__":
    main()
