import os
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from uuid import uuid4

class VectorStore:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = "handbook-chatbot"

        # Create index if not exists
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

        self.index = self.pc.Index(self.index_name)
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = PineconeVectorStore(index=self.index, embedding=self.embeddings)

    def add_documents(self, documents):
        uuids = [str(uuid4()) for _ in range(len(documents))]
        self.vector_store.add_documents(documents=documents, ids=uuids)
    
    def query(self, query, k=2):
        return self.vector_store.similarity_search(query, k=k)
