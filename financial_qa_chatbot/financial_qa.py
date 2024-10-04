import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate, LLMChain
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set the HuggingFace API token from the .env file
sec_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize the Streamlit application
st.title("Financial Query Assistant")

# Display an image
st.image("/Users/aameerkhan/Documents/GitHub/Noob-to-Ninja-ML/financial_qa_chatbot/assets/istockphoto-1432903655-612x612.jpg", use_column_width=True)

# Check if the token is loaded
if not sec_key:
    st.error("HuggingFace API token is not set. Please check your .env file.")
else:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = sec_key

    # Set up HuggingFaceEndpoint LLM
    repo_id = "mistralai/Mistral-Small-Instruct-2409"
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=sec_key, timeout=120)

    # Define the prompt template
    template = """ Question: {question}
    Answer: Please provide a detailed theoretical explanation, without any code or markdown formatting"""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create LangChain object
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Input field for the user to ask questions
    question = st.text_input("Enter your finance-related question:")

    # List of finance-related keywords to check
    finance_keywords = os.getenv("FINANCE_KEYWORDS").split(",")

    if st.button("Ask"):
        if question:
            # Check if the question contains any finance-related keywords
            if any(keyword.lower() in question.lower() for keyword in finance_keywords):
                # Get the response from the LLM
                response = llm_chain.run(question)
                # Display the response in Streamlit as plain text
                st.text("Answer: ")
                st.write(response)  # Use st.text to show it as plain text
            else:
                st.warning("Please ask a finance-related question.")
        else:
            st.write("Please enter a question.")

