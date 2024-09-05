# Langchain

## Objectifs

Les objectifs de ce lab sont de réaliser un premier appel à un des modèles mis à disposition par Vertex (**Gemini**), via langchain

Pour ce faire il faudra :
* Installer les librairies python langchain
* Installer les librairies complémentaires au client du LLM
* Renseigner son premier prompt

![INFO](../../img/info.png) Pour l'ensemble des labs, il est recommandé de travailler sur un environnement virtuel python. Il est même possible de travailler avec Jupiter directement intégré dans votre IDE pour une pleine pratique des labs.

## Recommendation

Pour l'ensemble des labs qui vont suivre, **il est recommandé de définir un environnement virtuel** que vous allez utiliser pour exécuter tous les labs qui vont suivre.
Pour ce faire dans votre espace de travail exécuter la commande suivante :

```sh
python3 -m venv .school.venv
```

Par la suite si vous revenez dans cet espace, n'oubliez pas de réactiver l'environnement virtuel via la commande suivante :

*Sous Linux :*
```sh
source .school.venv/bin/activate
```

*Sous Windows :*
```sh
.school.venv\Scripts\activate
```

> **Astuce 💡**: Lorsque l'environement virtuel est activé dans la session courante de votre terminal, son **nom devrait apparaitre au début de chaque ligne**, comme suit (ceci est exemple):
> 
> **(.school.venv)** node ➜ /workspaces/sfeir-school-langchain (main) $ 

## Installation

Via **pip**, installer les librairies `langchain` et `langchain-google-vertexai`. Celles-ci comprennent respectivement les modules/outils core pour créér des applications langchain, ainsi que les outils et extensions nécessaire à l'utilisation intégrations des LLMs disponnibles par Vertex.
Vertex utilisant l'authentification Google il nous faudra aussi installer `google.auth`.

```sh
pip install langchain langchain-google-vertexai google.auth
```

## Prérequis pour l'authentification

LangChain permettant de s'interfacer avec un grand nombre de LLMs, tout au long desLabs, nous allons utiliser ceux mis à disposition par Vertex. Pour cela il faudra renseigner des credentials comme ci-dessous.

```python
import os
import google.auth

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./path/to/file.json"

google.auth.default()
```

## Mon Premier script LangChain

Afin de réaliser notre premier appel à un LLM, nous utiliserons la librairie `langchain_google_vertexai`.

```python
from langchain_google_vertexai import VertexAI
```

Ensuite, à l'aide du constructeur *VertexAI()*, initialisez un objet qui permettra d'intérargir au travers du serveur Vertex AI avec un LLM en transmettant le prompt souhaité.

Dans le constructeur de notre objet VertexAI(), nous pouvons aussi ajouter différentes options.
Parmi lesquelles se trouvent :
- `model_name` (obligatoire) : Le nom du modeleur de LLM que l'on souhaite utiliser
- `temperature` (optionnel) : Contrôle le niveau d'aléatoire ou créativité dans les réponses

L'objet nouvellement définit par langchain fournit une méthode `invoke` pour déclencher un appel avec en paramètre notre demande.

[Liste des modèles disponibles dans Vertex](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models?hl=fr)