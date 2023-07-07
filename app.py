import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# レコーディング
audio_bytes = audio_recorder(pause_threshold=5.0)

def voice_to_text():
    # 音声データを一時的な音声ファイルに保存
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    # 音声ファイルの文字起こし
    with open("temp.wav", "rb") as f:
        transcript = openai.Audio.transcribe('whisper-1', f)
    
    return transcript['text']
    
if audio_bytes:
    st.write(voice_to_text())
