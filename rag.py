import sys
import os
import signal
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import google.generativeai as genai
import warnings
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

warnings.filterwarnings("ignore", category=FutureWarning)

def signal_handler(sig,frame):
    print("\nThanks for using gemini :)")
    sys.exit(0)
    
signal.signal(signal.SIGINT,signal_handler)

def generate_rag_prompt(query,context):
    escaped = context.replace("'","").replace('"',"").replace("\n"," ")
    prompt = ("""
You are a helpful and informative bot that answers questions using text from the reference context included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
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
        print(f"Error during similarity search: {e}")
    return context

def generate_answer(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

welcome_text = generate_answer("can you introduce yourself in a short paragraph?")
print(welcome_text)

while True:
    print("----------------------------------------------------------------------\n")
    print("What would you like to ask")
    query = input("Question: ")
    context = get_info_from_db(query)
    prompt = generate_rag_prompt(query=query,context=context)
    # print(prompt)
    answer = generate_answer(prompt=prompt)
    print(answer)
