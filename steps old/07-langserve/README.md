# LangChain - LangServe

## Objectifs

* Construire deux ChatBots (Mistral, CodeLLama)
* Construire la partie Backend d'exposition
* Définir un client de test de notre exposition

```mermaid
flowchart TD
    A[App]
    C((Client))
    C1(Chaine 1)
    C2(Chaine 2)
  
   subgraph LangServe
        A
        C1
        C2

        A --> |expose /chain1|C1
        A --> |expose /chain2|C2
        end
    
    C -->|requête|LangServe
```

## Etapes

### Deux chatbot

Construire à partir des labs précédents deux chats bots (ex: Mistral & LLama2).

### LangServe

Définir un fichier python `server.py`, qui va permettre d'exécuter LangServe.
Y créer deux routes associées chacunes à l'un des chatbots, via la méthode static **add_routes**

### Client

Proposition de client python :
Définir un client python **RemoteRunnable** du package *langserve*, (par exemple dans un notebook dédié). 
A partir de lui, définir une liste de messages, voire utiliser un *input* utilisateur. Construisez une écriture LCEL du prompt et des exécutables pour déclencher l'appel via la méthode **batch**.

![](..img/info.png) La classe **RunnableMap** permet de définir plusieurs *Runnable* en un seul.
