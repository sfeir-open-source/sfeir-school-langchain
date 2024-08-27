<!-- .slide: class=""-->

# LangChain

## LLMs

<br>

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

* LLMs et configurables

##==##

<!-- .slide:-->

# LangChainAgents

## Agents

<div style="display: flex;flex-direction: row;width: 100%">
<div style="flex: 1">

<br><br>

* Décisions basées sur les I/O d'un flux de travail

<br><br>

* Eventuelles connexions à des outils

<br><br>

* Orientation du flux, gestion d'erreurs et/ou d'exceptions
</div>
<div style="flex: 1;text-align: center">
<img class="h-800" src="./assets/images/agent_schema.png">
</div>
</div>

Notes:
- un agent utilise un LLM en moteur de résonnement pour déterminer quelle action effectuer et avec quels inputs
- peut utiliser des outils pour interragir avec son environnement ou effectuer des tâches

##==##

<!-- .slide:  class="exercice"-->

# 06 - LangChain

## Lab

* Création d'un agent et d'outils
