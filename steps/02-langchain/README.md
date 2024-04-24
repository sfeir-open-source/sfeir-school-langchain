# Langchain

## Objectifs

Les objectifs de ce lab sont de réaliser les mêmes appels au llm **llama2**, via langchain

* Installer les librairies python langchain
* installer les librairies complémentaires au client du LLM
* renseigner son premier prompt
* définir un premier parser de sortie

![INFO](../img/info.png) Pour l'ensemble des lab, il est recommandé de travailler sur un environnement virtuel python. Il est même possible de travailler avec Jupiter directement intégré dans votre IDE pour une pleine pratique des labs.

## Recommendation

Pour l'ensemble des labs qui vont suivre, il est recommandé de définir un environnement virtuel que vous allez utiliser pour exécuter tous les labs qui vont suivre.
Pour ce faire dans votre espace de travail exécuter la commande suivante :

```sh
python3 -m venv .school.venv
```

Par la suite si vous revenez dans cet espace, n'oubliez pas de réactiver l'environnement virtuel via la commande suivante :

```sh
source .school.venv/bin/activate
```

## Installation

Via pip, installer la librairie langchain. Celle-ci comprend déjà les packages pour ollama

```sh
pip install langchain
```

## Mon Premier script LangChain

Comme premier LLM, nous allons utiliser le serveur ollama précédemment installé/utilisé.
Pour notre premier script python, nous allons avoir besoin de la librairie _Ollama_ pour se connecter au LLM local. Cette librairie est directement inclus dans langchain dans le package _community_.

```python
from langchain_community.llms import Ollama
```

Ensuite, définissez une variable de définition de notre model **llama** (ou "mistral", un model précédemment pull dans ollama), en utilisant le constructeur _Ollama_. Cet objet va se charger d'intérargir au travers du serveur Ollama avec un LLM, en transmettant le prompt souhaité.

Pour se faire, l'objet définit par langchain fournit une méthode _invoke_ pour déclencher une séquence.

**Remarque :** S'assurer que le serveur _Ollama_ est toujours actif. Le temps de réponse dépendra fortement de votre carte graphique.
