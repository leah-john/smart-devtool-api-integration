from fastapi import FastAPI
from backend.app.crawler.crawler import crawl_documentation
from backend.app.rag.text_processor import clean_text, create_chunks
from backend.app.rag.vector_store import store_chunks
from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.services.llm_service import generate_answer
from backend.app.models.request_models import AnalyzeRequest
from backend.app.services.endpoint_extractor import extract_endpoints
from backend.app.services.auth_detector import detect_authentication
from backend.app.services.recommendation_engine import generate_recommendations
from backend.app.services.provider_detector import detect_provider
from backend.app.services.sdk_recommender import recommend_sdk
from backend.app.services.wrapper_generator import generate_wrapper

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
def analyze_documentation(request: AnalyzeRequest):

    raw_text = crawl_documentation(request.url)

    cleaned_text = clean_text(raw_text)

    endpoints = extract_endpoints(cleaned_text)

    auth_type = detect_authentication(cleaned_text)

    provider = detect_provider(cleaned_text)

    recommended_sdks = recommend_sdk(provider)

    filename = f"backend/generated_wrappers/{provider.lower()}_wrapper.py"

    wrapper_code = "Wrapper generation unavailable."

    try:
        wrapper_code = generate_wrapper(
            provider,
            auth_type,
            endpoints
        )
    except Exception:
        pass

    with open(filename, "w", encoding="utf-8") as file:
        file.write(wrapper_code)

    recommendations = "Recommendations unavailable."

    try:
        recommendations = generate_recommendations(
            auth_type,
            endpoints,
            request.use_case
        )
    except Exception:
        pass

    # RAG Storage
    chunks = create_chunks(cleaned_text)

    store_chunks(chunks)

    return {
        "message": "Documentation analyzed successfully",
        "total_chunks": len(chunks),
        "total_endpoints": len(endpoints),
        "provider": provider,
        "authentication": auth_type,
        "endpoints": endpoints,
        "recommendations": recommendations,
        "recommended_sdks": recommended_sdks,
        "wrapper_code": wrapper_code,
    }