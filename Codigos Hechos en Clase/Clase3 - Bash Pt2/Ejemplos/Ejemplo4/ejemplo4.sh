#!/bin/bash

numero=0

until [ $numero -gt 5 ] && [ $numero -lt 10 ]; do    
    numero=$(( (RANDOM % 20) + 1 ))
    echo "El valor actual del numero es: $numero"
done