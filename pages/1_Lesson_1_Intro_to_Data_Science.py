import streamlit as st
import pandas as pd
#from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 1 - Getting up to speed with Data Science", page_icon="📖", layout="wide")

#load_css()

with open(r'content\Lesson-1.md', 'r') as file:
    markdown_file_content = file.read()

st.markdown(markdown_file_content, unsafe_allow_html=True)
