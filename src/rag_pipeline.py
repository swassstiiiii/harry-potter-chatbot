from langchain_core.prompts import ChatPromptTemplate

from src.llm import get_llm
from src.retriever import retriever

llm = get_llm()

template = """
You are a Harry Potter expert.

Use ONLY the provided context.

Previous Conversation:
{chat_history}

Book Context:
{context}

Current Question:
{question}

Rules:
- Answer in 3-4 sentences.
- If the user asks follow-up questions like "he", "she", "his", "her", or "they", use the previous conversation to understand who they mean.
- If the answer isn't in the book, say:
"I couldn't find that information in the book."
"""

prompt = ChatPromptTemplate.from_template(template)


def get_answer(question, chat_history=""):

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    messages = prompt.invoke(
        {"context": context, "chat_history": chat_history, "question": question}
    )

    response = llm.invoke(messages)

    return response.content
