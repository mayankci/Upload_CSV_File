import pandas as pd
import streamlit as st

st.set_page_config(page_title="File Uploader")

# Function to upload file to Streamlit Cloud
@st.cache(allow_output_mutation=True)
def upload_to_streamlit_cloud(file):
    # Do something to upload the file to Streamlit Cloud
    return file

uploaded_file = st.file_uploader(label="Upload your dataset:")

if uploaded_file:
    st.write("File uploaded successfully!")
    
    if st.button("Submit"):
        # Upload the file to Streamlit Cloud
        uploaded_file = upload_to_streamlit_cloud(uploaded_file)
        st.write("File uploaded to Streamlit Cloud!")
