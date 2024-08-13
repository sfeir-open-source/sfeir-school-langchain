<!-- .slide: class="transition"-->

# 🦜🔗 Langchain

##==##

<!-- .slide:-->

# 🦜🔗 Langchain

- Harrison Chase et Ankush Gola ont lancé Langchain en Octobre 2022
<br><br>

- [GitHub - Open Source](https://github.com/langchain-ai/langchain) - ouverture  17 octobre 2022
<br><br>
- Framework de développement d'applications en lien avec les LLM
<br><br>
- Interconnexion de données et être agentique
<br><br>
<div class="flex-row">
    <img class="h-150" src="./assets/images/python.png">
    <img class="h-150" src="./assets/images/javascript.png">
</div>

Notes:
* agentique :capacité à prendre des décisions et à agir de manière autonome en ayant conscience de son environnement, en interagissant avec lui

##==##

<!-- .slide:-->

# Langchain - Concepts

<div style="display: flex;flex-direction: row;width: 100%">
<div style="flex: 1">

* Interface de multiples LLMs

<br><br>

* IA Privé ou public

<br><br>

* Utilisation de données externes

<br><br>

* Mise à disposition d'APIs et monitoring
</div>
<div style="flex: 1;display: flex;flex-direction: column;justify-content: center">
<img class="h-800" style="display: block;margin-left: auto;margin-right: auto" src="./assets/images/langchain_stack.svg">
<div style="text-align: center"><a href="https://python.langchain.com/v0.1/docs/get_started/introduction/" style="font-size: 14px; display: block">Source</a></div>
</div>
</div>

Notes:
LangChain est un framework conçu pour faciliter le développement d'applications utilisant des modèles de langage (LLMs)
La puissance de ce framework est dans sa capacité à gérer efficacement les interactions avec de multiples LLMs à travers des fonctionnalités comme la gestion des prompts, le chaînage, les agents, la mémoire et l'indexation. Son approche modulaire, sa flexibilité et son extensibilité en font un outil puissant pour développer une large gamme d'applications basées sur les LLMs de manière personnalisable et adaptable.

Il est possible d'utiliser des LLMs autant publiques que privés.
* llms publiques : providers ou APIs
* llms privés : hébergés en interne (éventuellement développés ou adaptés)

Enfin, LangChain peut mettre rapidement à disposition les chaînes ou agents développés au travers d'APIs permettant ainsi aux utilisateurs d'intégrer facilement ces fonctionnalités dans leurs flux de travail.
Ce framework existe dans plusieurs langages (principalement en Python et JavaScript, mais différents portages communautaires existent) permettant aux développeurs de choisir ce qui convient le mieux à leur application.

Bonus : D'autres projets similaires commencent à voir le jour sur d'autres langages comme par exemple Spring AI.

##==##

<!-- .slide:-->

# Langchain - Fonctionnalités

* Prompts et templates

<br><br>

* Chaînage de process

<br><br>

* Historique / données externes

<br><br>

* Agents et outils

Notes:
* prompts / templates : envoi des requêtes aux LLMs avec possibilité de variabiliser certaines parties du prompt
* chaînage : séquence d'appels avec un LLM, un outils ou un traitement de données => LCEL & ChainLCEL & Chain
* possibilité de garder en mémoire les précédentes intractions et de les prendre en compte dans les futurs appels
* agents : un modèle choisi la séquence d'actions à faire vs chaîne dont la séquence est figée dans le prompt

##==##

<!-- .slide:  class="exercice"-->

# 02 - LangChain

## Lab

* Mon Premier script

##==##

<!-- .slide:-->

# Langchain

<br>

## Première approche

* Les parsers : analyseur de données, principalement utilisé en sortie

<br><br>

* Les prompts : personnalisés ou via IA

<br><br>

* Les chaînes : séquence d'appels avec un LLM, un outils ou un traitement de données => LCEL

Notes:
* LCEL = LangChain Expression Language
* Interface définissant ```invoke, batch, stream, ainvoke, ..```

##==##

<!-- .slide:  class="exercice"-->

# 03 - LangChain

## Lab

* LangChain Expression Language

##==##

<!-- .slide:-->

# LangChain

<br>

## Seconde approche : modules d'interface

* Language Model : LLM ou ChatModel
<br><br>
* Les retrievers : récupèrent de données pour enrichir et augmenter la précision des requêtes
<br><br>
* les bases vectorielles : un stockage de données non structurées et vectorisées
<br><br>
* Les agents : un modèle choisissant la séquence d'actions à prendre vs chaîne dont la séquence est figée

Notes:
- LLM = input simple / ChatModel = input séquence de messages structurés
- Concept sortant NLP - Natural Language Programming

##==##

<!-- .slide:-->

# LangChain - Agents
## To move for later

* Prise de décision basée sur les I/O d'un flux de travail

<br><br>

* Orientation du flux, gestion d'erreurs et/ou d'exceptions

<br><br>

* Eventuelles connexions à des outils influençant la qualité de l'agent

##==##

<!-- .slide:-->

# Embedding : Principe

* Conversion de texte en vecteurs numériques denses
<br><br>
* Capture le sens et les relations entre les mots et phrases
<br><br>
* Permet la comparaison de textes et la recherche de similarités
<br>
<img src="./assets/images/embeddings.png">

Notes:

- Les embeddings permettent de représenter le texte de manière compréhensible pour les machines
- Cette représentation est cruciale pour la recherche et la comparaison de textes

##==##

<!-- .slide:-->

# Embedding : Recherche de similarités

<div style="display: flex; height: 80%; width: 100%; justify-content: center;">
<iframe src="https://openai.com/index/introducing-text-and-code-embeddings/#text-similarity-models" title="embeddings visualisation" frameborder="0"
style="width: 100%; height: 100%;"></iframe>
</div>
##==##

<!-- .slide:-->

# LangChain - Vector stores

* Stockage de données d'enrichissement

<div class="flex-row mt-100">
    <img class="h-150" src="./assets/images/pgvector.png">
    <img class="h-150" src="./assets/images/pinecone.png">
    <img class="h-150" src="./assets/images/faiss.png">
    <img class="h-150" src="./assets/images/redis.png">
</div>

* [Vector Stores compatibles](https://python.langchain.com/docs/integrations/vectorstores/)
<br><br>

* Attention à l'aspect bêta des interfaces

Notes:
exception bêta ChatMessageHistory
car essentiellement encore codé sur le moèdle Chain et non LCEL

##==##

<!-- .slide:-->

# LangChain - Retrievers

* Coeur principal des RAG (Retrieval Augmented Generation)

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
