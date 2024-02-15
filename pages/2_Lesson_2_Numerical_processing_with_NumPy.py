import streamlit as st
import pandas as pd
#from utilities import load_css, read_md

#st.set_page_config(page_title="Lesson 2 - Numerical processing with NumPy", page_icon="📖", layout="wide")

#load_css()
with open(r'content\Lesson-2.md', 'r') as file:
    md = file.read()

st.markdown(md, unsafe_allow_html=True)

