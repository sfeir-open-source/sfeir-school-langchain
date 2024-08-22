# Langchain - Chain

## Objectif

Pour ce lab, l'idée est de construire et de se familiriaser avec le principe de LCEL et de construire sa première chaîne.

```mermaid
flowchart LR
    A[Prompt] --> B[LLM]
    B --> C[Parser de String]
```

## Etapes

Sur la base du précédent lab, définir un llm relié à un modèle Ollama, par exemple "mistral".

Pour la chaîne on va rajouter un interpréteur et une nouvelle sortie de réponse pour embellir celle-ci.

<!-- ![schema](./assets/schema.png) -->

On va avoir besoin d'un template pour structurer le prompt que l'on va transmettre, **PromptTemplate**, du package `langchain_core.prompts`, va permettre de définir un template de notre input de messages. Il possède une méthode *`from_template`* qui va permetre via les attributs entre '{}' d'être injecté via notre chaîne d'interprétation.
Et pour la sortie afin d'avoir une réponse plus embellie, nous allons utiliser le parser *`StrOutputParser`*, du package `langchain_core.output_parsers`, sans options particulières.

Le chaînage LCEL se fait via l'operateur **'|'** entre les objets, que l'on affecte à une variable. Et ainsi appeler la méthode invoke avec les paramètres souhaités, correspondant en particulier au paramètres attendus définit dans notre template de prompt définit.

Vous devez arrivé à une écriture proche de celle-ci :

```python
chain = prompt | llm | output_parser
chain.invoke({"input":input})
```

## Aller plus loin

### Streaming

On peut stream la réponse, au lieu d'appeler la méthode *`invoke`*, utilisez la méthode *`stream()`*. 
Attention, cette méthode vous retourne un itérateur sur les morceaux de réponses quand ils sont disponibles, donc il va falloir boucler dessus et utiliser la méthode *`print()`* avec les options suivantes ```end="", flush=True```.

### ChatPrompt

```mermaid
flowchart TD
    SM1[Message système - contexte]
    SM2[Message système - instructions JSON]
    HM[Human Message]
    J(Structure JSON)
    P[Parser JSON]
    L[LLM]

    J -.-> SM2
    J -.-> P

    subgraph prompt
        SM1 --> SM2 --> HM
    end

    prompt --> L --> P
```

On peut trouver des prompts plus avancés tout comme les parsers. Essayez avec pour prompt : **ChatPromptTemplate** et pour parser : **JsonOutputParser**. Pour le second s'ajoute une complexité, où il va falloir donner dans le prompt, l'information que l'on souhaite la réponse dans un certain format, pour permettre l'interprétation et la structuration de la réponse correctement.

* Déjà structurez la réponse, en se basant sur la lib [**pydantic**](https://docs.pydantic.dev/1.10/)

```python
from langchain_core.pydantic_v1 import BaseModel, Field

class Response(BaseModel):
    answer: str = Field(description="answer to the user's question")
    source: str = Field(description="source used to answer the user's question, should be a website")
```

Définissons notre parser de sortie JSON en prenant en compte la structure attendue, en utilisant **JsonOutputParser** avec le paramètre *`pydantic_object`*.

Ensuite, on peut définir notre prompt en tant que **ChatPromptTemplate**. Au sein du prompt ne pas oublier d'ajouter un message de type **"system"**, permettant d'injecter les instructions du format de réponse. Ajouter en dernier message l'input de message qui va nous permettre de prendre en compte l'entrée au moment du lancement de la chaîne.

> **Astuce 💡:** **JsonOutputParser** a une méthode *`get_format_instructions()`* permettant de récupérer le format de l'objet sous forme d'instruction.

Chaîner les éléments et exécuter :

* le prompt de chat
* le llm désignant le model
* le parser de sortie

```python
chain = prompt | llm | parser
chain.invoke({"question": "What is the capital of Norway?"})

# {'answer': 'Oslo', 'source': 'https://en.wikipedia.org/wiki/Capital_city'}
```
