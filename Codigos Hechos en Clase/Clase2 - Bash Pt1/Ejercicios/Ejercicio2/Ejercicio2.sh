#!/bin/bash

cat ../Ejercicio1/Intro/Ejercicio/datos_personales.txt
cp ../Ejercicio1/Intro/Ejercicio/datos_personales.txt datos_personales_mod.txt
sed -i 's/soltero/casado/g' datos_personales_mod.txt
cat datos_personales_mod.txt
wc -c datos_personales_mod.txt
