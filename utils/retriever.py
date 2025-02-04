class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def get_relevant_documents(self, query):
        results = self.vector_store.query(query, k=2)
        return "\n\n".join([res.page_content for res in results])
