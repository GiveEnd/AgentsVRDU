import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title="Document Agent",
    version="0.1.0",
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://host.docker.internal:11434",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen3:8b",
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "ollama_url": OLLAMA_BASE_URL,
        "model": OLLAMA_MODEL,
    }


@app.get("/ollama")
async def ollama_status():
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{OLLAMA_BASE_URL}/api/tags"
        )

    response.raise_for_status()

    data = response.json()

    return {
        "status": "ok",
        "models": [
            model["name"]
            for model in data.get("models", [])
        ],
    }