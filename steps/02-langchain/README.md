# Langchain

## Objectifs

Les objectifs de ce lab sont de réaliser les mêmes appels au llm **llama2**, via langchain

* Installer les librairies python langchain
* installer les librairies complémentaires au client du LLM
* renseigner son premier prompt
* définir un premier parser de sortie

![INFO](../img/info.png) Pour l'ensemble des lab, il est recommandé de travailler sur un environnement virtuel python. Il est même possible de travailler avec Jupiter directement intégré dans votre IDE pour une pleine pratique des labs.

## Recommendation

Pour l'ensemble des labs qui vont suivre, **il est recommandé de définir un environnement virtuel** que vous allez utiliser pour exécuter tous les labs qui vont suivre.
Pour ce faire dans votre espace de travail exécuter la commande suivante :

```sh
python3 -m venv .school.venv
```

Par la suite si vous revenez dans cet espace, n'oubliez pas de réactiver l'environnement virtuel via la commande suivante :

```sh
source .school.venv/bin/activate
```
> **Astuce 💡**: Lorsque l'environement virtuel est activé dans la session courante de votre terminal, son **nom devrait apparaitre au début de chaque ligne**, comme suit (ceci est exemple):
> 
> **(.school.venv)** node ➜ /workspaces/sfeir-school-langchain (main) $ 

## Installation

Via **pip**, installer les librairies `langchain` et `langchain-community`. Celles-ci comprennent respectivement les modules/outils core pour créér des applications langchain, ainsi que les outils et extensions communautaires, comme les intégrations avec les LLMs `Ollama`, `OpenAI`, etc...

```sh
pip install langchain langchain-community
```

## Mon Premier script LangChain

Comme premier LLM, nous allons utiliser le serveur ollama précédemment installé/utilisé.
Pour notre premier script python, nous allons avoir besoin de la librairie _Ollama_ pour se connecter au LLM local.
Cette librairie est incluse dans le module `langchain-community`.

```python
from langchain_community.llms.ollama import Ollama
```

Ensuite, définissez une variable de définition de notre model **llama** (ou "mistral", un model précédemment pull dans ollama), en utilisant le constructeur _Ollama()_. Cet objet va se charger d'intérargir au travers du serveur Ollama avec un LLM, en transmettant le prompt souhaité.

Pour se faire, l'objet définit par langchain fournit une méthode _invoke_ pour déclencher une séquence.

**Remarque :** S'assurer que le serveur _Ollama_ est toujours actif. Le temps de réponse dépendra fortement de votre carte graphique et/ou si le serveur _Ollama_ tourne directement sur votre machine ou dans une image Docker (très lent).
