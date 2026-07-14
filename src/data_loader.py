from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/Harry-Potter-and-The-Philosophers-Stone.pdf")

documents = loader.load()

print(f"Total pages: {len(documents)}")

print("\nFirst page:\n")
print(documents[0].page_content)
for i in range(5):
    print(f"\n--- Page {i+1} ---")
    print(documents[i].page_content[:500])  # first 500 characters
