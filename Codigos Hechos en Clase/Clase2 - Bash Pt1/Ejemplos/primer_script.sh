#!/bin/bash

echo -n "ingrese una nota: "
read x

if [ $x -ge 4 ]; then
    echo "Aprobó el examen"
else
    echo "No aprobó el exámen pues su nota es menor a 4"
fi