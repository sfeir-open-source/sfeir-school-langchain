<!-- .slide: class="transition"-->

# 🦜🔗 Langchain

##==##

<!-- .slide:-->

# 🦜🔗 Langchain

- Harrison Chase et Ankush Gola a lancé Langchain en Octobre 2022
<br><br>

- [GitHub - Open Source](https://github.com/langchain-ai/langchain) - ouverture  17 octobre 2022
<br><br>
- Framework de développement d'outils, d'APIs en lien avec les LLM
<br><br>
- Interconnexion de données et être agentique
<br><br>
<div class="flex-row">
    <img class="h-150" src="./assets/images/python.png">
    <img class="h-150" src="./assets/images/javascript.png">
</div>

Notes:
* agentique :avoir conscience de son environnement, pouvoir intérargir avec lui => compétences autorégulatrices

##==##

<!-- .slide:  class="exercice"-->

# 02 - LangChain

## Lab

* Mon Premier script

##==##

<!-- .slide:-->

# Langchain - Concept

* Chaînage du process

<br><br>

* Retrieval Augmented Generation - RAG

##==##

<!-- .slide:-->

# Langchain

* Interface de multiple LLM

<br><br>

* IA Privé ou public

<br><br>

* Utilisation des API

Notes:
LangChain est une plateforme d'intelligence artificielle qui permet aux utilisateurs de créer et de gérer des modèles d'IA personnalisés pour différentes tâches, telles que la génération de texte, la reconnaissance d'images, la traduction automatique, etc.
Aspects clés de LangChain est son interface de multiple IA
Combinaison de multipple IA => personnalisation + précision + automatisation.

IA privés = fermés, entrainé pour soi, sur des données propres

Enfin, LangChain utilise des API pour permettre aux utilisateurs d'intégrer facilement des modèles d'IA dans leurs applications et leurs flux de travail. Les API de LangChain sont conçues pour être faciles à utiliser et à intégrer, ce qui permet aux utilisateurs de se concentrer sur la création de flux de travail personnalisés plutôt que sur la gestion de la complexité technique sous-jacente. Les API de LangChain prennent en charge une variété de langages de programmation, ce qui permet aux utilisateurs de choisir le langage qui convient le mieux à leur application.

##==##

<!-- .slide:-->

# Langchain

<br>

## Première approche

* les chaînes : la séquence d'appels avec un LLM, un outils ou un traitement de données => LCEL & Chain
<br><br>
* les parsers : analyseur de donnée, principalement utiliser en sortie
<br><br>
* les prompts : personnalisés ou via IA

Notes:
* LCEL = LangChain Expression Language
* Interface définissant ```invoke, batch, stream, ainvoke, ..```

##==##

<!-- .slide:  class="exercice"-->

# 03 - LangChain

## Lab

* LCEL

##==##

<!-- .slide:-->

# LangChain

<br>

## Seconde approche : modules d'interface

* Language Model : LLM ou ChatModel
<br><br>
* les agents : un modèle pour permettre le choix de la séquence d'actions à prendre vs chaîne dont la séquence est figée
<br><br>
* les bases vectorielles : un stockage de données non structurées
<br><br>
* les retrievers : les récupérateurs de données pour enrichire et augmenter la précision des requêtes

Notes:
    Concept sortant PNL - Programming Natural Language

##==##

<!-- .slide:-->

# LangChain - Agents

* prise de décision basée sur les I/O d'un flux de travail

<br><br>

* Orientation du flux, gestion d'erreurs et/ou d'exceptions

<br><br>

* Contiennent des connexions à des outils influençant la qualité de l'agent

##==##

<!-- .slide:-->

# LangChain - Bases vectorielles

* Stockage de données d'enrichissement

<div class="flex-row mt-100">
    <img class="h-150" src="./assets/images/pgvector.png">
    <img class="h-150" src="./assets/images/pinecone.png">
    <img class="h-150" src="./assets/images/faiss.png">
    <img class="h-150" src="./assets/images/redis.png">
</div>

* [Vector Stores](https://python.langchain.com/docs/integrations/vectorstores/)
<br><br>

* Attention à l'aspect bêta des interfaces

Notes:
exception bêta ChatMessageHistory
car essentiellement encore codé sur le moèdle Chain et non LCEL

##==##

<!-- .slide:-->

# LangChain - Retrievers

* Coeur pricinpale des RAG (Retrieval Augmented Generation)

* Interprétation des données

![](./assets/images/langchain_retrieval.jpg)
[LangChain - Retrieval](https://python.langchain.com/docs/modules/data_connection/)
<!-- .element: class="credits" -->

##==##

<!-- .slide:  class="exercice"-->

# 04 - LangChain

## Lab

* Retrieval

##==##

<!-- .slide: class=""-->

# LangChain - LLMs

<div class="flex-row">
    <img src="./assets/images/mistral-ai.png">
    <img class="h-250" src="./assets/images/llama2.png">
</div>
<br><br>
<div class="flex-row">
    <img src="./assets/images/gemini.png">
    <img class="h-200" src="./assets/images/chatgpt.png">
    <img src="./assets/images/bedrock.png">
    <img class="h-200" src="./assets/images/dall-e.png">
</div>

[LLM](https://python.langchain.com/docs/integrations/llms/) | 
[Chat](https://python.langchain.com/docs/integrations/chat/) | 
[Embedding](https://python.langchain.com/docs/integrations/text_embedding)
<!-- .element: class="credits" -->

##==##

<!-- .slide:  class="exercice"-->

# 05 - LangChain

## Lab

* LLMs
