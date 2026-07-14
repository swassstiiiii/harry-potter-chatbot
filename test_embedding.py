from src.embeddings import get_embedding_model

embedding = get_embedding_model()

response = embedding.embed_query("Hello")

print("Embedding length:", len(response))
print(response[:5])
