from fastapi import FastAPI

app = FastAPI(title="DevOps Lab")

@app.get("/")
def home():
    return {
        "status": "success", 
        "message": "DevOps Pipeline"
    }

@app.get("/health")
def health_check():
    return {"status": "OK"}