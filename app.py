import streamlit as st
from src.rag_pipeline import get_answer

st.set_page_config(page_title="Harry Potter Chatbot", page_icon="⚡", layout="centered")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("⚡ Harry Potter Chatbot")

st.write("Welcome to the Hogwarts Express!")

st.sidebar.title("🪄 Hogwarts")

st.sidebar.write("""
Ask questions only about:

📖 Harry Potter and the Philosopher's Stone
""")

for chat in st.session_state.chat_history:

    st.info(f"🧑 You: {chat['question']}")

    st.success(f"🤖 {chat['answer']}")
question = st.text_input("Ask your question", placeholder="Example: Who is Hagrid?")

if st.button("⚡ Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        history = ""

        for chat in st.session_state.chat_history:
            history += f"User: {chat['question']}\n"
            history += f"Assistant: {chat['answer']}\n\n"

        with st.spinner("Thinking..."):
            answer = get_answer(question, history)

        st.session_state.chat_history.append({"question": question, "answer": answer})

        st.success("Answer found!")

        st.markdown("## 🤖 Answer")

        st.write(answer)
