import streamlit as st
import os
import google.generativeai as palm

st.title("Generative AI Text Generator")

# Get API key from environment variable
api_key = os.environ.get('APIKEY')

# Function to generate text
def generate_text(prompt):
    palm.configure(api_key=api_key)
    response = palm.generate_text(prompt=prompt)
    return response.result

# Streamlit UI elements
prompt = st.text_input("Enter your prompt:", "Once upon a time")
if st.button("Generate Text"):
    with st.spinner("Generating..."):
        generated_text = generate_text(prompt)
        st.success("Text Generated Successfully!")
        st.text_area("Generated Text:", generated_text)

st.write("Powered by Generative AI from Google")
