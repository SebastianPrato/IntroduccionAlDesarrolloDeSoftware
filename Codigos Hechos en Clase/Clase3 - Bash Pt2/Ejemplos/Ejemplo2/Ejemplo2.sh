#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Se debe pasar un directorio por parametro" 
    exit 1
fi

directorio=$1

if [ ! -d "$directorio" ]; then
    echo El parámetro no es un directorio válido
    exit 1
fi

for i in "$directorio"/*.txt; do 
    if [ -f "$i" ]; then
        echo "" #salto de linea
        echo "Contenido del archivo $i:"
        cat $i
        echo "" #salto de linea
    fi
done