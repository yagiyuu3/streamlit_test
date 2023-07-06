import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr

r = sr.Recognizer()

audio_bytes = audio_recorder(pause_threshold=5.0)

if audio_bytes:
    audio_data = sr.AudioData(audio_bytes, 44100, 2)
    try:
        text = r.recognize_google(audio_data, language='ja-JP')
        st.write(text)
    except sr.UnknownValueError:
        st.error("音声を認識できませんでした。もう一度お試しください。")
    except sr.RequestError as e:
        st.error(f"Google Speech Recognition APIからエラーが返されました: {e}")
