from fastapi import FastAPI
from src.copymate_ai.api.v1 import endpoints

app = FastAPI(title="Copymate AI Service")
app.include_router(endpoints.router, prefix="/api/v1", tags=["v1"])

@app.get("/")
def root():
    return {"message": "Hello from Copymate AI API!"}
