from langchain_chroma import Chroma
from src.embeddings import get_embedding_model

vectorstore = Chroma(
    persist_directory="vectordb", embedding_function=get_embedding_model()
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

query = "Who is Hagrid?"

results = retriever.invoke(query)

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}\n")
    print(doc.page_content)
    print("-" * 80)
