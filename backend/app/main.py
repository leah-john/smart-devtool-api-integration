from fastapi import FastAPI
from backend.app.crawler.crawler import crawl_documentation
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