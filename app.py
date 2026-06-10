import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Streamlit UI
st.title("🤖 Gemini Chatbot")

user_input = st.text_input("Ask a question:")

if user_input:
    try:
        response = llm.invoke(user_input)
        st.write(response.content)
    except Exception as e:
        st.error(f"Error: {e}")
