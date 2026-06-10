import os
from fastapi import FastAPI
from app.crawler.crawler import crawl_documentation
from app.rag.text_processor import clean_text, create_chunks
from app.rag.vector_store import store_chunks
from app.rag.retriever import retrieve_relevant_chunks
from app.services.llm_service import generate_answer
from app.models.request_models import AnalyzeRequest
from app.services.endpoint_extractor import extract_endpoints
from app.services.auth_detector import detect_authentication
from app.services.recommendation_engine import generate_recommendations
from app.services.provider_detector import detect_provider
from app.services.sdk_recommender import recommend_sdk
from app.services.wrapper_generator import generate_wrapper
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Smart DevTool API Integration",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    print("\n===== CLEANED TEXT SAMPLE =====")
    print(cleaned_text[:3000])

    print("\n===== ENDPOINTS =====")
    print(extract_endpoints(cleaned_text))

    print("\n===== AUTH =====")
    print(detect_authentication(cleaned_text))

    endpoints = extract_endpoints(cleaned_text)

    auth_type = detect_authentication(cleaned_text)

    provider = detect_provider(cleaned_text)

    recommended_sdks = recommend_sdk(provider)

    # Create folder automatically if missing
    os.makedirs("generated_wrappers", exist_ok=True)

    filename = (
        f"generated_wrappers/"
        f"{provider.lower()}_wrapper.py"
    )

    wrapper_code = "Wrapper generation unavailable."

    try:
        wrapper_code = generate_wrapper(
            provider,
            auth_type,
            endpoints
        )
    except Exception as e:
        print("Wrapper Generation Error:", e)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(wrapper_code)

    recommendations = "Recommendations unavailable."

    try:
        recommendations = generate_recommendations(
            auth_type,
            endpoints,
            request.use_case,
            cleaned_text[:3000]
        )
    except Exception as e:
        print("Recommendation Error:", e)

    chunks = create_chunks(cleaned_text)

    store_chunks(chunks)

    return {
        "message": "Documentation analyzed successfully",
        "provider": provider,
        "authentication": auth_type,
        "endpoints": endpoints,
        "recommended_sdks": recommended_sdks,
        "recommendations": recommendations,
        "wrapper_file": f"{provider.lower()}_wrapper.py",
        "download_url": f"/download-wrapper/{provider.lower()}"
    }


@app.get("/download-wrapper/{provider}")
def download_wrapper(provider: str):

    filename = (
        f"generated_wrappers/"
        f"{provider.lower()}_wrapper.py"
    )

    if not os.path.exists(filename):
        return {
            "error": "Wrapper file not found"
        }

    return FileResponse(
        path=filename,
        filename=f"{provider.lower()}_wrapper.py",
        media_type="text/plain"
    )