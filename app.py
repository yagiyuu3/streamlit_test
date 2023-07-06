import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import noisereduce as nr
import numpy as np

r = sr.Recognizer()

audio_bytes = audio_recorder(pause_threshold=5.0)

if audio_bytes:
    # Convert audio bytes to numpy array
    audio_np = np.frombuffer(audio_bytes, np.int16)
    
    # Reduce noise
    reduced_noise = nr.reduce_noise(audio_clip=audio_np, noise_clip=audio_np, verbose=False)
    
    # Convert numpy array to audio data
    audio_data = sr.AudioData(reduced_noise.tobytes(), 44100, 2)
    
    try:
        text = r.recognize_google(audio_data, language='ja-JP')
        st.write(text)
    except sr.UnknownValueError:
        st.error("音声を認識できませんでした。もう一度お試しください。")
    except sr.RequestError as e:
        st.error(f"Google Speech Recognition APIからエラーが返されました: {e}")
