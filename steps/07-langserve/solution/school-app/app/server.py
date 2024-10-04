from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

from langchain_google_vertexai import VertexAI
from chain.chain import get_chain

import os
import google.auth


# Gestion credentials VertexAI
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

google.auth.default()

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Ajout d'une route pour un LLM simple
add_routes(app, VertexAI(model_name="gemini-pro", temperature=0.1), path="/vertex")


# Ajout d'une route pour une chaîne
add_routes(app, get_chain(), path="/mychain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
