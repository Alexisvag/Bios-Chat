import os
from dotenv import load_dotenv

load_dotenv()

# =====================
# MODELOS
# =====================

LLM_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# =====================
# RAG CONFIG
# =====================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 4

# =====================
# VECTOR STORE
# =====================

FAISS_PATH = "faiss_index"

# =====================
# API KEY
# =====================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")