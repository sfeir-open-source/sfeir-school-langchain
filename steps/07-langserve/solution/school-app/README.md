# 🦜🔗 LangServe App

## Pré-requis

* Python 3.11
* Librairie de gestion `Poetry`

## Build

Utilisation de `poetry` pour gérerl'application

```sh
# active venv
poetry shell

# install
poetry install
```

## Run

```sh
# set GOOGLE_APPLICATION_CREDENTIALS
export GOOGLE_APPLICATION_CREDENTIALS=***********************

# run langserve
poetry run chain serve --port 8100
```

Pour voir le playground et jouer avec les API exposé accéder à l'URL, il y a deux chaînes disponibles.

* Une route simple directe : http://127.0.0.1:8100/vertex/playground/
* La route vers la chaîne customisée : http://127.0.0.1:8100/mychain/playground/