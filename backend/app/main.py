from fastapi import FastAPI
from backend.app.crawler.crawler import crawl_documentation
from backend.app.rag.text_processor import clean_text, create_chunks
from backend.app.rag.vector_store import store_chunks
from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.services.llm_service import generate_answer
from backend.app.models.request_models import URLRequest

app = FastAPI(
    title="Smart DevTool API Integration",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Smart DevTool Backend Running"
    }

@app.get("/crawl")
def crawl():

    url = "https://developer.paypal.com/docs/api"

    content = crawl_documentation(url)

    return {
        "content": content
    }

@app.get("/chunks")
def chunks():

    url = "https://developer.paypal.com/docs/api"

    content = crawl_documentation(url)

    cleaned_text = clean_text(content)

    chunks = create_chunks(cleaned_text)
    stored_count = store_chunks(chunks)

    return {
        "total_chunks": len(chunks),
        "stored_chunks": stored_count,
        "first_chunk": chunks[0]
    }

@app.get("/search")
def search():

    query = "How do I authenticate?"

    results = retrieve_relevant_chunks(query)

    return {
        "query": query,
        "results": results
    }
@app.get("/ask")
def ask():

    question = "How do I authenticate with PayPal?"

    retrieved_chunks = retrieve_relevant_chunks(question)

    context = "\n".join(retrieved_chunks)

    answer = generate_answer(
        question,
        context
    )

    return {
        "question": question,
        "answer": answer
    }
@app.post("/analyze")
def analyze_documentation(request: URLRequest):

    raw_text = crawl_documentation(request.url)

    cleaned_text = clean_text(raw_text)

    chunks = create_chunks(cleaned_text)

    store_chunks(chunks)

    return {
        "message": "Documentation analyzed successfully",
        "total_chunks": len(chunks)
    }