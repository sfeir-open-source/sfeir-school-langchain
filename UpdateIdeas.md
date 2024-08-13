# Things to do / update

## Todo list
- [ ] Correctif purement textuel / syntaxique dans les slides / tp
- [ ] Update technique sur les tps
- [ ] Ajouter une partie sur l'embedding
    - [ ] Qu'est ce que l'embedding ? A quoi ça sert ?
    - [ ] Comment ça fonctionne ? (Schéma 3D avec des vecteur pour imager + recherche de similarités)
- [ ] Parler plus des BDD vectorielles
    - Enrichir la partie des vector stores ?
    - [ ] Ajouter un tp avec ChromaDB ?

## Remarques à la relecture
- 00 - school -> RAS
- 10 - IA -> RAS
- 20 - Langchain -> DONE
    - Inverser les slides "Langchain" et "Langchain - Concept" : Présenter ce qu'est Langchain avant de présenter ce à quoi ça sert
    - Proposition de changement sur la définition d'agentique
    - Lab n°2 (réalisation d'un appel à Langchain) après la présentation de Langchain et avant la partie "Concepts"
    - Liste plus exhautive des concepts
    - Surement déplacer la slide sur les Agents pour en parler de manière plus approfondie plus tard
    - Caller les slides sur l'embedding juste avant la partie "Vector stores"
    - Proposition alternative pour le Lab n°4 sur la partie avec retriever
    - Eventuellement ajouter une slide sur les DB vectorielles (Pinceone / ChomaDB / etc.) entre "Retrivers" et "LLMs" (partie enlevée dans "Seconde approche" un peu plus détaillée)
    - Un Lab n°4.5 sur les DB vectorielles ?
    - Dans la slide "LLMs" peut être plus expliciter la notion de configurables
    - Renommer le Lab n°5 en "Configurable LLMs" plutôt que juste "LLMs"
- 30 - Applications -> DONE
    - Transformer le Lab n°6 en Lab sur les Agents et Tools
- 40 - Tools -> DONE
    - LangServe : RAS
    - LangGraph :
        - Schéma un peu complexe (simplifiable ?)
        - En faire juste une ouverture pour une 2ème journée en Institute ?
    - LangSmith : RAS

## Idées pour les Labs :
- 1 : LLM en local / avec vertex et requête de base (20 min)
- 2 : Chaines avec template et parser (20 min)
- 3 : Document loader (30 min)
- 4 : BDD vectorielle (ChromaDB) avec un RAG complet (30 min)
- 5 : Les configurables (20 min)
- 6 : Agent et tools (30 min)
- 7 : LangServe (30 min) -> Peut être juste en démo ?