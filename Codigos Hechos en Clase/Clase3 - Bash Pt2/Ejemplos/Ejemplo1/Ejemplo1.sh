#!/bin/bash

if [ $# -lt 1];then
    echo "Debe ingresar como parámetro el nombre de algún archivo"
    exit 
fi

archivo=$1
opc=0

while [ "$opc" != "4" ]; do
    echo "Seleccione una opción"
    echo "1. - Ver contenido del archivo"
    echo "2. - Editar el archivo"
    echo "3. - Ver permisos del archivo"
    echo "4. - Salir"

    read opc

    case $opc in
        1)
            cat "$archivo"
            ;;
        2) 
            nano "$archivo"
            ;;
        3)
            ls -l "$archivo"
            ;;
        4)
            echo "adiuss, gracias por usar este script"
            ;; 
        *)
            echo "Opción Inválida, intente nuevamente"

    esac

    echo ""

done