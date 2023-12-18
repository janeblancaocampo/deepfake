import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, ClientSettings
import librosa.display
import matplotlib.pyplot as plt
import io

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_data = []

    def recv(self, frame):
        if frame:
            audio_chunk = frame.to_ndarray(dtype="int16")
            self.audio_data.extend(audio_chunk)
        return frame

def process_uploaded_audio(uploaded_file):
    audio_data = io.BytesIO(uploaded_file.read())

    st.write("### Uploaded Audio Waveform:")
    audio, sr = librosa.load(audio_data, sr=None)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio, sr=sr)
    st.pyplot()

def main():
    st.title('Audio File Uploader and Recorder')

    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    st.write("OR")
    recording_state = webrtc_streamer(
        key="audio-recorder",
        mode=ClientSettings.Mode.SENDRECV,
        audio=True,
        processor_factory=AudioProcessor,
    )

    if audio_file is not None:
        st.write("File uploaded successfully!")
        if st.button('Process Uploaded Audio'):
            process_uploaded_audio(audio_file)

    if recording_state:
        st.write("Recording...")

if __name__ == "__main__":
    main()
