#!/bin/bash

total=0
for (( i = 0; i < 5; i++)); do
    echo "Por favor ingrese una nota"
    read nota
    total=$((total + nota))
done
promedio=$((total/5))
echo "el promedio de las notas dadas es de: $promedio"