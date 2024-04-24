import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure GenAI with API key

# Function to get response from Gemini
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_prompt:
        response = model.generate_content([input_prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Gemini Image Demo")
st.title("Gemini Application")

# Input prompt and image upload
input_prompt = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to generate response
if st.button("Tell me about the image"):
    if image is not None:
        response = get_gemini_response(input_prompt, image)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please upload an image before requesting a response.")
