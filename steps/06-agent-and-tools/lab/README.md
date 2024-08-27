# LangChain - Agents et outils

## Objectifs

- Utiliser un outil fourni par LangChain
- Créer et utiliser un outil personnalisé
- Créer un agent capable d'utiliser ces outils
- Exécuter une requette sur cette agent et constater l'utilisation des outils

## Les outils

Les outils sont des composants qui permettent à un agent d'éffectuer des tâches spécifiques. Cela peut être un calcul mathématique, un recherche sur internet ou même l'appel à un service externe.

### Outils existants

Afin de facilité le développement des agents, LangChain et la communauté participant à son développement ont mis à disposition un certain nombre d'outils prêts à l'emploi (cf : [Liste des outils](https://python.langchain.com/v0.2/docs/integrations/tools/)).
Parmi ces outils, certains permettent de faire des recherches sur internet dont un en particulier : [DuckDuckGo Search](https://python.langchain.com/v0.2/docs/integrations/tools/ddg/) qui est entièrement gratuit d'utilisation.

### Outils customs

Parfois il peut être nécessaire de créer soit même un outil afin de répondre à un besoin spécifique.
Pour cela il faut créer un méthode possédant l'annotation `@tool`.
Cette méthode devra avoir une description qui permetra à l'agent de savoir dans quel contexte utiliser cet outil.
De plus afin que l'agent l'utilise au mieux il est préférable de typer correctement les paramètres d'entrée.

```python
@tool
def get_sentence_length(sentence: str) -> int:
    """Returns the length of a sentence.""" # description de ce que fait l'outil

    print("Determining the length of a given sentence...")
    return len(sentence)
```

## Les agents

### Template de promp

Au même titre que pour une chaîne, il est possible de définir un template de prompt pour un agent. Ce template est même nécessaire car 3 variables sont obligatoire pour le bon fonctionnement de l'agent. Ces variables sont, dans l'ordre :

- `chat_history` : stocke l'historique des messages échangés entre l'utilisateur et l'agent. Cela permet à l'agent de maintenir le contexte de la conversation et de founir des réponses plus cohérentes.

- La requête de l'utilisateur via un `HumanMessage` ou un `HumanMessagePromptTemplate`

- `agent_scratchpad` : est utilisé pour stocker des informations temporaires / intermédiares dans le traitement de la requête. Cela peut inclure les étapes de raisonnement de l'agent, les résultats intermédiaires des outils, ou toute autre information utile pour la génération de la réponse finale.


__Exemple basique :__
```python
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant",
        ),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad", optional=True),
    ]
)
```

### Création de l'agent

Afin de créer un agent dans LangChain il suffit d'utiliser la méthode `create_tool_calling_agent` à laquelle il faudra fournir les paramètres suivants :
- `llm` : le `Chat Model` à utiliser. Il faut en utiliser un qui puisse prendre en charge l'appel à des outils (cf : [liste des modèles compatibles](https://python.langchain.com/v0.1/docs/integrations/chat/))
- `tools` : la liste des outils dont l'agent pourra se servir
- `prompt` : le template de prompt que l'on souhaite utiliser


### Contexte d'exécution

Dans l'état actuel, l'agent ne peut effectuer aucune action et nécessite l'utilisation d'un `AgentExecutor` qui va orchestrer le traitement de la requête ainsi l'exécution des outils.


### Appel à l'agent

Une fois l'`AgentExecutor` défin, il est possible d'interragir avec l'agent au travers de ce dernier. Cet `AgentExecutor` implémentant la même interface que le reste des composants chaînnables de LangChain, il suffit d'appeler la méthode `invoke` avec notre requête en input.

## Etapes

### Partie sans agent
1. Déclarer l'outil _DuckDuckGo Search_
2. Créer un outil _multiply_ qui retournera la multiplication de deux nombres entiers passés en paramètres
3. Exécuter ces 2 outils sans agent

### Partie avec agent
1. Rédiger le template de prompt pour l'agent
2. Création de la liste d'outils à partir ce ceux utiliser précédemment
3. Instantier l'agent avec le template de prompt et la liste d'outils et un `ChatModel`
4. Ajouter l'`AgentExecutor`
5. Exécuter une requête qui utilisera un des outils