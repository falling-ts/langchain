import streamlit as st
import os

def __readCssFile(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = f"{current_dir}/css/{file}"  # 指定 CSS 文件的路径，根据您的实际情况调整
    with open(css_path, "r") as f:
        css_content = f.read()
    return css_content


def common():
    css = __readCssFile('common.css')

    st.write(f"<style>{css}</style>", unsafe_allow_html=True)
