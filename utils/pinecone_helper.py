import pinecone
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME

pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
index = pinecone.Index(PINECONE_INDEX_NAME)

def store_embedding(id, embedding):
    index.upsert([(id, embedding)])

def get_similar_embeddings(query_embedding):
    return index.query(query_embedding, top_k=5, include_values=True)
