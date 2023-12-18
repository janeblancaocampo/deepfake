import streamlit as st
from io import BytesIO
from pydub import AudioSegment

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Display the uploaded file
        st.audio(uploaded_file, format='audio/mp3')

if __name__ == "__main__":
    main()
