import os
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import google.generativeai as genai
import warnings
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

warnings.filterwarnings("ignore", category=FutureWarning)

def generate_rag_prompt(query, context):
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""
You are a helpful and informative bot that answers questions using text from the reference context included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and conversational tone. \
  If the context is irrelevant to the answer, you may ignore it.
                QUESTION: '{query}'
                CONTEXT: '{context}'
              
              ANSWER:
              """).format(query=query, context=context)
    return prompt

def get_info_from_db(query):
    context = ""
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
    vectorStore = Chroma(persist_directory="./chroma_db_store", embedding_function=embedding)
    try:
        search_result = vectorStore.similarity_search(query, k=6)
        for results in search_result:
            context += results.page_content + "\n"
    except Exception as e:
        st.error(f"Error during similarity search: {e}")
    return context

def generate_answer(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

def main():
    st.title("RAG APP: QnA For CSE 🧑‍💻")

    welcome_text ="Hello! I am an AI-driven chatbot trained in various Computer Science subjects, including DBMS, Computer Networks, Operating Systems, and Object-Oriented Programming, Blockchain. Feel free to ask me any questions!"

    st.write(welcome_text)

    query = st.text_input("What would you like to ask:")
    if query:
        context = get_info_from_db(query)
        prompt = generate_rag_prompt(query=query, context=context)
        answer = generate_answer(prompt=prompt)
        st.write(answer)

if __name__ == "__main__":
    main()
