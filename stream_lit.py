import os
import requests
from google.cloud import storage
import streamlit as st

# Function to fetch client_secrets.json from GitHub
def fetch_client_secrets():
    # URL of the client_secrets.json file in your GitHub repository
    github_url = 'https://raw.githubusercontent.com/mayankci/Upload_CSV_File/main/client_secrets.json'
    response = requests.get(github_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Fetch client secrets from GitHub
client_secrets = fetch_client_secrets()

if client_secrets:
    # Set environment variable for Google Cloud service account credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secrets.json"

    # Create a GCS client
    client = storage.Client()

    # Function to upload file to Google Cloud Storage
    def upload_to_gcs(file, bucket_name, destination_blob_name):
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(file)
        return f"gs://{bucket_name}/{destination_blob_name}"

    st.title("File Uploader to Google Cloud Storage")

    # File upload widget
    uploaded_file = st.file_uploader("Upload CSV file")

    if uploaded_file:
        st.write("File uploaded successfully!")
        if st.button("Submit"):
            # Upload file to GCS
            file_url = upload_to_gcs(uploaded_file, 'your_bucket_name', 'your_destination_blob_name')
            st.write(f"File uploaded to Google Cloud Storage: {file_url}")
else:
    st.error("Failed to fetch client_secrets.json from GitHub. Please ensure the file is accessible.")
