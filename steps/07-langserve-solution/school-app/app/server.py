from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain_community.chat_models.ollama import ChatOllama

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, ChatOllama(model="mistral", temperature=1), path="/mistral")
add_routes(app, ChatOllama(model="llama2", temperature=1), path="/llama")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
