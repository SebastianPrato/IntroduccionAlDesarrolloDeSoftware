#!/bin/bash

contador=1;

while [ $contador -lt 6 ]; do
    echo "Bienvenido por vez número $contador"
    contador=$((contador+1));
done