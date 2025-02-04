from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_documents(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    
    # Split into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=4)
    docs = text_splitter.split_documents(documents)
    
    return docs
