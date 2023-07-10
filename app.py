import streamlit as st
import streamlit.components.v1 as stc
import base64
import time

button = st.button('アプリ実行')
if button:
    audio_path1 = 'sample.wav' #入力する音声ファイル
    audio_placeholder = st.empty()
    file_ = open(audio_path1, "rb")
    contents = file_.read()
    file_.close()
    audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    audio_html = """<audio autoplay=True><source src="%s" type="audio/ogg" autoplay=True>Your browser does not support the audio element.</audio>""" %audio_str
    audio_placeholder.empty()
    time.sleep(0.5) #これがないと上手く再生されません
    audio_placeholder.markdown(audio_html, unsafe_allow_html=True
