import streamlit as st
import pyttsx3
import tempfile

st.set_page_config(page_title="Text-to-Speech App", page_icon=":microphone:")

st.title("Text-to-Speech App")

input_text = st.text_area("Enter Text Here")
voice = st.selectbox("Select Voice", ["en", "ja"])

if st.button("Speak"):
    if input_text:
        engine = pyttsx3.init()
        engine.setProperty('voice', voice)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            fname = f.name
            engine.save_to_file(input_text, fname)
            engine.runAndWait()
            st.audio(fname, format="audio/wav")
    else:
        st.warning("Please enter some text.")
