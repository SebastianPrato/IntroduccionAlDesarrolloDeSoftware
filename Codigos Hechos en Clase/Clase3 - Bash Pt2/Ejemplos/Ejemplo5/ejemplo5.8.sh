#!/bin/bash

echo archivo original:
echo ''
cat archivo.txt
echo ''
sed -i 's/hola/hiii~/g' archivo.txt
echo archivo editado:
cat archivo.txt
echo ''
sed -i 's/hiii~/hola/g' archivo.txt
archivo revirtiendo la edición:
cat archivo.txt
echo ''
