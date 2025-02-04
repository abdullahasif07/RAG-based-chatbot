import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate

class LLMModel:
    def __init__(self):
        self.repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        self.llm = HuggingFaceEndpoint(
            repo_id=self.repo_id,
            temperature=0.8,
            top_k=50,
            huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY')
        )

        self.template = """
        You are a chatbot designed to answer questions from LUMS students. Use the provided context to answer the question. 
        If the context is not relevant, say "I don't know."
        
        Context: {context}
        Question: {question}
        Answer:
        """

        self.prompt = PromptTemplate(template=self.template, input_variables=["context", "question"])

    def generate_response(self, question, context):
        formatted_prompt = self.prompt.format(context=context, question=question)
        return self.llm.invoke(formatted_prompt)
