import os
import dotenv
import streamlit as st
from chatbot import ChatBot

# Load environment variables
dotenv.load_dotenv()

# Initialize chatbot
chatbot = ChatBot()

# Streamlit UI
st.title("LUMS Handbook ChatBot")
user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_input:
        response = chatbot.answer_question(user_input)
        st.write(response)
    else:
        st.write("Please enter a question.")
