from utils.data_loader import load_documents
from utils.vector_store import VectorStore
from utils.retriever import Retriever
from utils.model import LLMModel

class ChatBot:
    def __init__(self):
        self.vector_store = VectorStore()
        self.retriever = Retriever(self.vector_store)
        self.llm = LLMModel()
    
    def answer_question(self, question):
        context = self.retriever.get_relevant_documents(question)
        if not context:
            return "I don't know."
        return self.llm.generate_response(question, context)
