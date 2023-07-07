import streamlit as st
from audio_recorder_streamlit import audio_recorder
import whisper
    
# モデルの読み込み
model = whisper.load_model("base")

# レコーディング
r = sr.Recognizer()

audio_bytes = audio_recorder(pause_threshold=5.0)

if audio_bytes:
    audio_data = sr.AudioData(audio_bytes, 44100, 2)

    # 音声ファイルの文字起こし
    result = model.transcribe(audio_data)

    # 結果の表示
    st.write(result["text"])
