from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

import os
import google.auth

from langchain_google_vertexai import VertexAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Ajout d'une route pour un LLM simple
add_routes(app, VertexAI(model_name="gemini-pro", temperature=0.1), path="/vertex")


# Ajout d'une route pour une chaîne
prompt = PromptTemplate.from_template(
    "Explique moi simplement le concept suivant : {topic}"
)
llm = VertexAI(model_name="gemini-pro", temperature=0.1)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
add_routes(app, chain, path="/mychain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
