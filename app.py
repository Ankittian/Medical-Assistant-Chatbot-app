from flask import Flask, render_template, request, jsonify
from src.helper import download_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Home route
@app.route("/")
def index():
    return render_template("chatbot.html")

embeddings=download_embedding("sentence-transformers/all-MiniLM-L6-v2")

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY



from pinecone import Pinecone
pinecone_api_key=PINECONE_API_KEY
pc= Pinecone(api_key=pinecone_api_key)

from pinecone import ServerlessSpec

index_name="medical-assistant-chatbot"

vector_store= PineconeVectorStore.from_existing_index(
    embedding=embeddings,
    index_name=index_name
    )

retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={"k":5})

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    
)

medical_rag_chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        system_prompt
    ),
    (
        "human",
        """
Context:
{context}

Question:
{input}
"""
    )
])

question_answering_chain = create_stuff_documents_chain(model, medical_rag_chat_prompt)
main_chain= create_retrieval_chain(retriever, question_answering_chain)

# Chat API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message received"}), 400

    msg = data["message"].strip()
    print("User input:", msg)

    response = main_chain.invoke({"input": msg})
    answer = response.get("answer", "No answer generated.")

    print("Response:", answer)
    return jsonify({"reply": answer})
    



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)