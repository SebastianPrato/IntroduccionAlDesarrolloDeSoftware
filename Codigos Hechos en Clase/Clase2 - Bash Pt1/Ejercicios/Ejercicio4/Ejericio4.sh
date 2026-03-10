#!/bin/bash

ruta="$1"


if [ -f "$ruta" ]; then
  echo "Es un archivo, procedermos a mostrar su contenido"
  cat $ruta
elif [ -d "$ruta" ]; then
  echo "Es un directorio, procederemos a listar los archivos que contiene:"
  cd $ruta
  ls
else
  echo "No es ni un archivo ni un directorio válido"
fi


