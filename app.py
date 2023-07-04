import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
if audio_bytes:
    audio = r.record(audio_bytes)
    text = r.recognize_google(audio, language='ja-JP')
    st.write(text)
