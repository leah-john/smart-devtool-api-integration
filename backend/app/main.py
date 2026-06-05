from fastapi import FastAPI

app = FastAPI(
    title="Smart DevTool API Integration",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Smart DevTool Backend Running"
    }