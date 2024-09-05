<!-- .slide:-->

# LangChain

## Seconde approche : modules d'interface

<br><br>

* Language Model : LLM ou ChatModel
<br><br>
* les bases vectorielles : un stockage de données non structurées et vectorisées
<br><br>
* Les retrievers : récupèrent de données pour enrichir et augmenter la précision des requêtes
<br><br>
* Les agents : un modèle choisissant la séquence d'actions à prendre vs chaîne dont la séquence est figée

Notes:
- LLM = input simple / ChatModel = input séquence de messages structurés
- Concept sortant NLP - Natural Language Programming

##==##

<!-- .slide:-->

# LangChain

## Données externes

<div style="display: flex;flex-direction: row;width: 100%">
<div style="flex: 1">

<br><br>

* Récupération depuis diverses sources

<br><br>

* Retour sous la forme d'un ou plusieurs <a href="https://js.langchain.com/v0.2/docs/concepts/#document">documents</a>

<br><br>

* Problématiques de traitement des données
</div>
<img class="h-800" src="./assets/images/document_loading.png">
</div>

Notes:
- document : interface de langchain pour la représentation de données textuelles
    - pageContent : contenu de la page
    - metadata : informations additionnelles (source, date, données custom, ...)

##==##

<!-- .slide: class="exercice"-->

# 03 - LangChain

## Lab

* Données externes
