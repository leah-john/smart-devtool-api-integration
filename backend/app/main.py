from fastapi import FastAPI
from backend.app.crawler.crawler import crawl_documentation
from backend.app.rag.text_processor import clean_text, create_chunks
from backend.app.rag.vector_store import store_chunks

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