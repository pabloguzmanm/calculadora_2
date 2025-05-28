
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.markdown("<style>body { margin: 0; }</style>", unsafe_allow_html=True)

with open("calculadora.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1000, scrolling=True)
