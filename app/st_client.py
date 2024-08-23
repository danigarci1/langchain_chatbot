import streamlit as st
import base64
from langserve import RemoteRunnable

# Set up the Streamlit app
st.title("Process File client")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Read the uploaded file
    file_data = uploaded_file.read()

    # Encode the file data to base64
    encoded_data = base64.b64encode(file_data).decode("utf-8")

    # Define the endpoint URL
    chat_service_url = "https://localhost:8000/pdf"

    # Create a RemoteRunnable instance
    chat = RemoteRunnable(chat_service_url)

    # Send the encoded data to the endpoint
    with st.spinner("Analizing file. Please wait..."):
        response = chat.invoke({"file": encoded_data})
    
    # Display the response
    st.subheader("Result:")
    st.json(response)
