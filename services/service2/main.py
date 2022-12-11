from fastapi import FastAPI
import requests
import os

app = FastAPI(
    title = 'Service 2',
    version='1.0',
)

# Health check the current service
@app.get("/health")
async def health_check():
    return {
        "message": "Hello from service 2"
    }

# Communicate with the other service
@app.get("/talk")
async def communicate():
    
    url = os.getenv("SERVICE1_URL") + "/health"
    resp = requests.get(url,timeout=5)
    print(resp.json())
    return resp.json()