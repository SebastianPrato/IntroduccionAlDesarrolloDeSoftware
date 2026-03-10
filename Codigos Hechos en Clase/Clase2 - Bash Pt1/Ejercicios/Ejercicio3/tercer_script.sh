#!/bin/bash

echo -n Ingrese el tipo de extensión que deseas buscar: 
read ext

ls | grep -e '.*'$ext