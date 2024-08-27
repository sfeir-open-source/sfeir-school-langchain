<!-- .slide: class="transition"-->

# Les outils Langchain

##==##

<!-- .slide:-->

# 🦜️🏓 LangServe

* Deploiement des éléments exécutables et des chaines LangChain en tant que API REST
<br><br>

* FastAPI + pydantic
<br><br>

* Swagger + RemoteRunnable (python, JS)
<br><br>

* /invoke, /stream, /batch, ...
<br><br>

* /playground - UI simple de configuration

Notes:
pydantic => Validation des données

##==##

<!-- .slide: class="with-code-bg-dark" -->

# 🦜️🏓 LangServe

## Backend
<br>

### langchain-cli : construction de deux espaces = packages / app

```python
# app/server.py
from fastapi import FastAPI
from langserve import add_routes
from my_chain.chain import chain as my_chain

app = FastAPI()

add_routes(app, my_chain)
```

<br>

### Exécution

```bash
#!/bin/bash
langchain serve
```

[Playground - http://localhost:8000/<my-app>/playground](http://localhost:8000/<my-app>/playground)

Notes:
Définition des CORS
Sécurité - Attention à l'exposition du playground
Exécution via **uvicorn** possible si __main__

##==##

<!-- .slide: class="with-code-bg-dark" -->

# 🦜️🏓 LangServe

## Client

* Utilisation du SDK (Python, JS)

```python
from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chat")

chain.invoke({"topic": "Nantes"})
```

* Via **requests** (Python)

* Curl

```bash
curl --location --request POST 'http://localhost:8000/chat/invoke' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "input": {
            "topic": "Badminton"
        }
    }'
```

Notes:
Déploiement sur Cloud Run, AWS Copilot, Azure en mode serverless directement

##==##

<!-- .slide:  class="exercice"-->

# 07 - 🦜️🏓 LangServe

## Lab

##==##

<!-- .slide:-->

# 🦜🕸️ LangGraph

* Une librairie de l'écosystème LangChain
<br><br>

* Pilote multi-agent comme une machine à état
<br><br>

* Mise en place d'interconnexions entre des agents (WorkFlow, Node)
<br><br>

* Workflow de cycles

<!-- ## ==## -->

<!-- <!-- .slide: class="cadre no-filter langgraph-steps" data-type-show="prez" data-state="langgraph-steps"-->
<!-- # LangGraph -->

<!-- <svg class="h-850">
    <use href="#langgraph-multi-agent" link:href="#langgraph-multi-agent" />
</svg> -->
<!-- <div class="fragment" data-fragment-index="1" hidden></div>
<div class="fragment" data-fragment-index="2" hidden></div>
<div class="fragment" data-fragment-index="3" hidden></div>
<div class="fragment" data-fragment-index="4" hidden></div>
<div class="fragment" data-fragment-index="5" hidden></div>
<div class="fragment" data-fragment-index="6" hidden></div>
<div class="fragment" data-fragment-index="7" hidden></div>
<div class="fragment" data-fragment-index="8" hidden></div>
<div class="fragment" data-fragment-index="9" hidden></div> -->
