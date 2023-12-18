import streamlit as st

def main():
    st.title('Audio File Uploader')

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        # You can perform further processing or analysis with the uploaded file here

if __name__ == "__main__":
    main()
