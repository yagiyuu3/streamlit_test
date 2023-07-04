import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
 
r = sr.Recognizer()

audio_bytes = audio_recorder(pause_threshold=5.0)

if audio_bytes:
#     audio_data = sr.AudioData(audio_bytes, 44100, 2)
#     text = r.recognize_google(audio_data, language='ja-JP')
    st.write("text")
