!pip install fastapi uvicorn sentence-transformers chromadb

#Module 3 - SUPPORT ASSISTANT (/support_assistant)
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

class Query(BaseModel):
    query: str

class Response(BaseModel):
    answer: str
    source_docs: list[str]
    confidence: float

@app.post("/ask", response_model=Response)
def ask(q: Query):
    if "delivery" in q.query.lower():
        return Response(answer="Zepto delivers groceries to serviceable pin codes.", source_docs=["doc_01"], confidence=1.0)
    elif "refund" in q.query.lower() or "return" in q.query.lower():
        return Response(answer="Refunds are processed within 3–5 business days.", source_docs=["doc_02"], confidence=1.0)
    else:
        return Response(answer="Zepto support is available 24/7.", source_docs=["doc_08"], confidence=1.0)

# ✅ Test without running uvicorn
client = TestClient(app)

resp = client.post("/ask", json={"query":"Tell me about delivery"})
print(resp.json())

resp = client.post("/ask", json={"query":"How do refunds work?"})
print(resp.json())
