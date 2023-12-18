import pydub
import streamlit as st
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Check if the file type is supported
        if uploaded_file.type == "audio/mp3" or uploaded_file.type == "audio/wav" or upload_file.type == "audio/m4a":
            audio_bytes = uploaded_file.read()
            st.audio(audio_bytes, format=uploaded_file.type)

            # Play the audio
            st.write("Playing the audio...")
            audio_segment = AudioSegment.from_file(BytesIO(audio_bytes))
            play(audio_segment)

        else:
            st.write("Uploaded file type not supported. Please upload an MP3, M4A or WAV file.")

if __name__ == "__main__":
    main()
