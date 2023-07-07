import streamlit as st
from audio_recorder_streamlit import audio_recorder
import whisper
import wave

# モデルの読み込み
model = whisper.load_model("base")

# レコーディング
audio_bytes = audio_recorder(pause_threshold=5.0)

if audio_bytes:
    # 音声データを一時的な音声ファイルに保存
    with wave.open("temp.wav", "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
        f.writeframes(audio_bytes)

    # 音声ファイルの文字起こし
    result = model.transcribe("temp.wav")

    # 結果の表示
    st.write(result["text"])
