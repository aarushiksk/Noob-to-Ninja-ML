import streamlit as st
import os
import google.generativeai as palm

st.title("Generative AI Text Generator")

# Get API key from environment variable
api_key = os.environ.get('APIKEY')

# Function to generate text
def generate_text(prompt):
    try:
        if api_key is None:
            raise ValueError("API key is not provided. Set the 'APIKEY' environment variable.")
        
        palm.configure(api_key=api_key)
        response = palm.generate_text(prompt=prompt)
        
        if response.status_code == 200:
            return response.result
        else:
            raise Exception(f"Text generation failed with status code {response.status_code}.")
    
    except ValueError as ve:
        st.error(str(ve))
        return None

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit UI elements
prompt = st.text_input("Enter your prompt:", "Once upon a time")
if st.button("Generate Text"):
    with st.spinner("Generating..."):
        generated_text = generate_text(prompt)
        if generated_text is not None:
            st.success("Text Generated Successfully!")
            st.text_area("Generated Text:", generated_text)

st.write("Powered by Generative AI from Google")
