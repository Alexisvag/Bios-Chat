from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings
from config.settings import FAISS_PATH

import os


def build_vector_store(chunks):

    embeddings = get_embeddings()

    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    if os.path.exists(FAISS_PATH):

        vector_store = FAISS.load_local(
            FAISS_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vector_store

    return None