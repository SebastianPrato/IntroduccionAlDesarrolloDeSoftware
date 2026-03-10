#!/bin/bash

if [ -d "TP2-IDS" ]; then
    echo "El entorno ya ha sido creado!"
    exit 0
fi

mkdir TP2-IDS
cd TP2-IDS || exit
mkdir static templates src
mkdir static/css static/images
pipenv install flask
touch src/app.py
echo "Proyecto creado con éxito. Inicializa el entorno con: pipenv shell"