from src.data_loader import documents
from src.preprocessing import chunks
from src.vector_store import create_vector_store

print("Documents:", len(documents))
print("Chunks:", len(chunks))

vectorstore = create_vector_store(chunks)

print("Stored:", vectorstore._collection.count())
