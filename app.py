from flask import Flask, render_template, request

from dotenv import load_dotenv

from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from medical_chatbot.helper import downlaod_hugging_face_embeddings
from medical_chatbot.prompt import system_prompt

load_dotenv()

app = Flask(__name__)

INDEX_NAME = "medical-bot"
embedding_model = downlaod_hugging_face_embeddings()
docsearch = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embedding_model,
)
retriever = docsearch.as_retriever(search_type='similarity', search_kwargs={'k': 3})

llm = OpenAI(temperature=0.3, max_tokens=500)


prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('user', "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = rag_chain.invoke({"input": msg})
    return str(response["answer"])




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

