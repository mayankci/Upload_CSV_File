import pandas as pd 
import numpy as np  
import streamlit as st 


st.set_page_config(page_title="File Uploader")

df = st.file_uploader(label="Upload your dataset:")

if df:
    df = pd.read_csv(df)
    
    st.write(df.head())
