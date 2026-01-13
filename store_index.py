from helper import load_pdf, filter_doc, split_documents, download_embedding
import os

from dotenv import load_dotenv
load_dotenv()


data=load_pdf("Data")
filtered_documents = filter_doc(data)
text_chunks=split_documents(filtered_documents)
embeddings=download_embedding("sentence-transformers/all-MiniLM-L6-v2")

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


from pinecone import Pinecone
pinecone_api_key=PINECONE_API_KEY
pc= Pinecone(api_key=pinecone_api_key)

from pinecone import ServerlessSpec

index_name="medical-assistant-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name= index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

index=pc.Index(index_name)

from langchain_pinecone import PineconeVectorStore

