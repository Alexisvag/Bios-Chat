# 📄 Bios Chat — Analizador de Documentos

## 📌 Descripción

Este proyecto implementa una aplicación basada en **RAG (Retrieval Augmented Generation)** que permite cargar documentos y realizar preguntas sobre su contenido utilizando un modelo de lenguaje **LLM (Large Language Model)**, garantizando que las respuestas se generen únicamente a partir de la información contenida en los archivos cargados, evitando alucinaciones.

Formatos soportados:

- PDF
- DOCX
- XLSX
- TXT

La solución fue desarrollada con una arquitectura modular similar a la utilizada en sistemas reales de IA.

---

## 🧠 Arquitectura de la solución

La aplicación sigue una arquitectura RAG:

Usuario → Interfaz Streamlit → Cargador de documentos → Splitter → Embeddings → FAISS → Retriever → Prompt → LLM (Gemini) → Respuesta

### Componentes

| Capa | Tecnología |
|-------|-----------|
| Interfaz | Streamlit |
| LLM | Google Gemini |
| Embeddings | HuggingFace |
| Vector Store | FAISS |
| Framework | LangChain (LCEL) |
| Configuración | dotenv |
| Lenguaje | Python |

### Flujo

1. El usuario carga un archivo
2. Se extrae el texto
3. Se divide en fragmentos
4. Se generan embeddings
5. Se crea índice FAISS
6. Retriever busca contexto relevante
7. Prompt incluye contexto
8. LLM genera respuesta
9. Se muestra en chat

---

## 📂 Estructura del proyecto

```
bios-chat/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env (no incluido)
│
├── config/
│ └── settings.py
│
├── rag/
│ ├── embeddings.py
│ ├── vectorstore.py
│ ├── pipeline.py
│ ├── prompt.py
│
├── loaders/
├── utils/
├── faiss_index/

```

---

## ⚙️ Instalación

Clonar repositorio:

```bash
git clone https://github.com/Alexisvag/Bios-Chat.git
cd Bios-Chat
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar:

Windows
```bash
.venv\Scripts\activate
```

Linux / Mac
```bash
source .venv/bin/activate
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

🔑 Variables de entorno

Obtener API Key:

https://aistudio.google.com/app/apikey

▶️ Ejecutar la aplicación
```bash
streamlit run app.py
```
Abrir en navegador:

```bash
http://localhost:8501
```

Subir documento y hacer preguntas.

✅ Funcionalidades

- Carga de múltiples formatos (PDF, DOCX, XLSX, TXT)
- Arquitectura RAG (Retrieval Augmented Generation)
- Fragmentación automática de documentos
- Generación de embeddings semánticos
- Almacenamiento vectorial con FAISS
- Búsqueda semántica de contexto relevante
- Generación de respuestas con LLM (Gemini)
- Control de alucinaciones mediante prompt restringido
- Interfaz tipo chat con Streamlit
- Arquitectura modular por capas

🧪 Ejemplos de preguntas

PDF / DOCX / TXT
- ¿Cuál es el tema principal?
- Resume el documento
- ¿Qué conclusiones hay?
- ¿Qué datos se mencionan?

XLSX
- ¿Qué columnas tiene?
- ¿Qué valores contiene?
- ¿Cuál es el promedio?
- ¿Cuántos registros hay?

🧩 Decisiones técnicas

- Uso de arquitectura RAG  
Permite generar respuestas basadas en contexto recuperado, reduciendo alucinaciones.

- FAISS  
Uso de FAISS como base vectorial local por su alto rendimiento y facilidad de integración.

- HuggingFace Embeddings  
Uso de embeddings livianos (all-MiniLM-L6-v2) por su eficiencia y compatibilidad con FAISS.

- Gemini  
Uso de Gemini como LLM por su buen rendimiento y fácil integración mediante API.

- Streamlit  
Uso de Streamlit para construir una interfaz interactiva tipo chat de forma rápida.

- dotenv  
Uso de variables de entorno para manejar credenciales de forma segura.

- LangChain (LCEL)  
Uso de LangChain Expression Language para construir pipelines RAG modulares.

- Text Splitter  
Fragmentación automática de documentos para mejorar la recuperación semántica.

- Prompt control  
Uso de prompts restringidos para obligar al modelo a responder solo con el contexto.

🚀 Posibles mejoras futuras

- Memoria conversacional
- Persistencia de índices
- API con FastAPI
- Dockerización
- Autenticación
- Multiusuario
- Despliegue en nube
- Logging
- Tests unitarios
- Streaming de respuestas
- Filtros por metadata

