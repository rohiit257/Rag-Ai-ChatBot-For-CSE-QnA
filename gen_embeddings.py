from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

loaders = [PyPDFLoader('')]

docs = []

for file in loaders:
    docs.extend(file.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 100)
docs = text_splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2",model_kwargs ={'device':'cpu'})

vectorStore = Chroma.from_documents(docs,embedding,persist_directory="./chroma_db_store")

print(vectorStore._collection.count())