import os

from dotenv import load_dotenv
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore


from medical_chatbot.helper import load_pdf_file, split_text, downlaod_hugging_face_embeddings


load_dotenv()


extracted_data = load_pdf_file("data/")
text_chunks = split_text(extracted_data)
embedding_model = downlaod_hugging_face_embeddings()


pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
index_name = "medical-bot"

pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embedding_model
)


