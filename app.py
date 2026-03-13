import streamlit as st

from loaders.document_loader import extract_text
from rag.vectorstore import build_vector_store
from rag.pipeline import build_rag_chain
from utils.session import init_chat

from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


st.set_page_config(page_title="Bios Chat")

st.title("Analista de Documentos")

import streamlit as st

st.title("BIOS CHAT RAG")

api_key = st.text_input(
    "Ingrese su API Key de Gemini",
    type="password"
)

init_chat()

uploaded_files = st.file_uploader(
    "Inserta un documento",
    type=["pdf","docx","xlsx","txt"],
    accept_multiple_files=True
)

if uploaded_files:

    text = ""

    for file in uploaded_files:
        text += extract_text(file)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_text(text)

    vector_store = build_vector_store(chunks)

    retriever = vector_store.as_retriever()

    rag_chain = build_rag_chain(retriever)

    user_question = st.chat_input("Pregunta sobre el documento")

    if user_question:

        response = rag_chain.invoke(user_question)

        st.write(response)