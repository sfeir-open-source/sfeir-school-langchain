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
- sortie officielle octobre 2022 mais travail préalable sur GPT-1 et 2
- framework conçu pour faciliter le développement d'applications utilisant des LLMs
- simplifie l'interaction avec les APIs des LLMs existants
- framework existants en Python et JavaScript
- agentique : capacité à prendre des décisions et à agir de manière autonome en ayant conscience de son environnement, en interagissant avec lui

Bonus : D'autres projets similaires commencent à voir le jour sur d'autres langages comme par exemple Spring AI.

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
- gère efficacement les interactions avec plusieurs LLMs grâces à ses fonctionnalités
- approche modulaire, flexible et extensible
- possibilité d'utiliser des LLMs publiques ou privés
    - llms publiques : providers ou APIs
    - llms privés : hébergés en interne (éventuellement développés ou adaptés)
- données externes -> enrichissement des requêtes faites aux LLMs
- mise à disposition au travers d'APIs
- monitoring

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
