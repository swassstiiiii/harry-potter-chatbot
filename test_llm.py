from src.llm import get_llm

llm = get_llm()

response = llm.invoke("Who is Harry Potter?")

print(response.content)
