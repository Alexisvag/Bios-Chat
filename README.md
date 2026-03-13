# 📄 Bios Chat — Analizador de Documentos

## 📌 Descripción

Este proyecto implementa una aplicación basada en **RAG (Retrieval Augmented Generation)** que permite cargar documentos y realizar preguntas sobre su contenido utilizando un modelo de lenguaje (LLM), garantizando que las respuestas se generen únicamente a partir de la información contenida en los archivos cargados, evitando alucinaciones.

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

- Carga de múltiples formatos
- Arquitectura RAG
- Búsqueda semántica
- Respuestas sin alucinaciones
- Configuración modular
- Uso de variables de entorno
- Separación por capas
- Interfaz tipo chat

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

- Uso de RAG
- Permite evitar alucinaciones al usar contexto recuperado.
- FAISS
- Base vectorial rápida y local.
- HuggingFace Embeddings
- Modelo liviano y eficiente.
- Gemini
- Buen rendimiento y fácil integración.
- Streamlit
- Interfaz rápida para pruebas.
- dotenv
- Manejo seguro de credenciales.
- LangChain LCEL
- Arquitectura moderna para pipelines LLM.

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

