import openai
import pinecone
from config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_INDEX_NAME

class Chatbot:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
        self.index = pinecone.Index(PINECONE_INDEX_NAME)

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
