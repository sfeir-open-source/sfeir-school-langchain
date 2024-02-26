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

<!-- .slide:-->

# LangGraph

* Une librairie de l'echo-système LangChain
<br><br>

* pilote multi-agent comme une machine à état
<br><br>

* Mise en place d'interconnexion entre des agents
<br><br>

* Workflow de cycles

##==##

<!-- .slide:-->

# LangGraph

TODO graphique multi-agent avec routeur

##==##

<!-- .slide: class="full-center" -->

# LangSmith

![h-900](./assets/images/langsmith.png)

##==##

<!-- .slide: -->

# LangSmith

* [LangSmith - https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)
<br><br>

* self-managed
![h-100](./assets/images/docker.png)
![h-100](./assets/images/kubernetes.png)
<br><br>

* 3 Offres de pricing
<br><br>

* Gestion des prompts, Monitoring, Tokens
<br><br>

* Evaluation, Etiquette

<!-- .element: class="credits" -->

Notes:
Pricing Dev, Plus, Enterprise

Feature SSO (Enterprise)
