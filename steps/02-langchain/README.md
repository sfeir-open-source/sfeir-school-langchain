# Langchain

## Objectifs

Les objectifs de ce lab sont de réaliser les mêmes appels au llm **llama2**, via langchain

* Installer les librairies python langchain
* installer les librairies complémntaires au client du LLM
* renseigner son premier prompt
* définir un premier parser de sortie

![INFO](../img/info.png) Pour l'ensemble des lab, il est recommandé de travailler sur un environnement virtuel python. Il est même possible de travailler avec Jupiter directement intégré dans votre IDE pour une pleine pratique des labs.

## Installation

Via pip, installer la librairie langchain. Celle-ci comprends déjà les packages pour ollama

```sh
pip install langchain
```

## Mon Premier script LangChain

Comme premier LLM, nous allons utiliser le serveur ollama précédemment installé/utilisé.
Pour notre premier script python, nous allons avoir besoin de la librairie _Ollama_ pour se connecter au LLM local. Cette librairie est directement inclu dans langchain dans le package _community_.

```python
from langchain_community.llms import Ollama
```

Ensuite, définissez une variable de définition de notre model **llama** (ou "mistral", un model précédemment pull dans ollama), en utilisant le constructeur _Ollama_. Cet objet va se charger d'intérargir au travers du serveur Ollama avec un LLM, en transmettant le prompt souhaité.

Pour se faire, l'objet définit par langchain fournit une méthode _invoke_ pour déclencher une séquence.

**Remarque :** S'assurer que le serveur _Ollama_ est toujours actif. Le temps de réponse dépendra fortement de votre carte graphique.
