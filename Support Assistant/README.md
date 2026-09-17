# Support Assistant API

A lightweight, local Support Assistant API built with **FastAPI** to handle customer support queries (e.g., delivery, refunds) and provide structured responses. 

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Data Validation:** Pydantic
* **Testing:** FastAPI TestClient
* **Embeddings & Vector Database:** Sentence-Transformers & ChromaDB *(Ready for future RAG scaling)*

---

## 🚀 Getting Started

### 1. Installation
Clone your repository, navigate to the project directory, and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running the Script & Tests
You can run the script directly to execute the built-in integration tests without spinning up a full Uvicorn server:
```bash
python main.py
```

### 3. Launching the API Server
To start the live development server and test using interactive API docs:
```bash
uvicorn main:app --reload
```
Once the server is running, open your browser and navigate to:
* **Interactive Swagger UI Docs:** [http://127.0.0](http://127.0.0)
* **Alternative API Docs (ReDoc):** [http://127.0.0](http://127.0.0)

---

## 🔌 API Endpoints

### **POST** `/ask`
Submits a user query to the support assistant.

* **Request Body:**
```json
{
  "query": "Tell me about delivery"
}
```

* **Response Body (200 OK):**
```json
{
  "answer": "Zepto delivers groceries to serviceable pin codes.",
  "source_docs": ["doc_01"],
  "confidence": 1.0
}
```
