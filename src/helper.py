from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from typing import List
from langchain.schema import Document

def load_pdf(data):
    loader= DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents


def filter_doc(docs: List[Document]) -> List[Document]:
    """
    Filters a list of LangChain documents to retain only 
    page_content and the 'source' field from metadata.
    """
    filtered_docs = []
    
    for doc in docs:
        # Extract the source, defaulting to "Unknown" if the key doesn't exist
        source_info = doc.metadata.get("source")
        
        # Create a new Document object with restricted metadata
        new_doc = Document(
            page_content=doc.page_content,
            metadata={"source": source_info}
        )
        filtered_docs.append(new_doc)
        
    return filtered_docs
    
def split_documents(documents):
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks=text_splitter.split_documents(documents)
    return chunks

from langchain.embeddings import HuggingFaceEmbeddings

def download_embedding(model_name: str):
    model=model_name
    embeddings=HuggingFaceEmbeddings(
        model_name=model,
    )
    return embeddings


