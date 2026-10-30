from pathlib import Path

import streamlit as st
from components.process import process

# Styling lives in style.css
st.markdown(f"<style>{Path('style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# sentiment -> (comment, icon)
RESPONSES = {
    "positive": ("Great vibes! Keep it up.", "😊"),
    "neutral": ("Nothing strong either way.", "😐"),
    "negetive": ("That sounds rough. Hope things get better.", "😞"),
}

st.markdown('<div class="app-title">Sentiment Analysis App</div>', unsafe_allow_html=True)

with st.container(key="input_panel"):
    text = st.text_input("Enter the Sentence :")
    clicked = st.button("Sentimentize", key="analyze_btn")

if clicked:
    with st.spinner("Identifying the sentiment..."):
        result = process(text)

    comment, icon = RESPONSES[result.strip().lower()]
    st.markdown(f'<div class="badge {result.strip().lower()}">{icon} {result.upper()}</div>', unsafe_allow_html=True)
    with st.container(key="result_panel"):
        st.write(comment)