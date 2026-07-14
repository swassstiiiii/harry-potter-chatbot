from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.data_loader import documents

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print(type(chunks))
print(type(chunks[0]))
print(chunks[0].metadata)
