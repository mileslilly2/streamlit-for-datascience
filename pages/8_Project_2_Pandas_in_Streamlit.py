import streamlit as st
import pandas as pd
#from utilities import load_css, read_md

st.set_page_config(page_title="Project 2 - Using Pandas in Streamlit", page_icon="🛠️", layout="wide")

with open(r'content\Project-2.md', 'r') as file:
    md = file.read()
st.markdown(md, unsafe_allow_html=True)
