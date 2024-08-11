import streamlit as st

from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
file_path = '<path to Object_casedocs>'

loader = DirectoryLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
   chunk_size=1000,
   chunk_overlap=20,
   length_function=len,
   is_separator_regex=False,
)

documents = text_splitter.split_documents(docs)

llm = Ollama(model="llama3")
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Create Chroma vector store
vector_store = Chroma.from_documents(documents, embedding=embeddings)

# Load the QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

query = st.text_input("Enter your question")
response = qa_chain.run(query)

st.write(response)