import streamlit as st
from audio_recorder_streamlit import audio_recorder

# レコーディング
audio_bytes = audio_recorder(pause_threshold=5.0)

def voice_to_text():
    transcript = openai.Audio.transcribe('whisper-1', audio_bytes)
    return transcript['text']
    
if audio_bytes:
    st.write(voice_to_text())
