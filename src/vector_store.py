from langchain_chroma import Chroma
from src.embeddings import get_embedding_model


def create_vector_store(chunks):
    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=get_embedding_model(), persist_directory="vectordb"
    )

    return vectorstore
