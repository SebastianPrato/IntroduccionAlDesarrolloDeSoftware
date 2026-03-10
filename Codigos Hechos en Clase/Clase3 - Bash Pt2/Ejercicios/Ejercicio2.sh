#!/bin/bash

opc=0

while [ $opc -ne 5 ]; do

    echo "Ingrese una opcion"
    echo "1. - Censurar palabra"
    echo "2. - Abrir el archivo"
    echo "3. - Realizar una copia del archivo llamada menu_copia.sh"
    echo "4. - Valida email"
    echo "5. - Salir"
    read opc

    case $opc in
        1) 
            echo Ingrese la palabra que desea censurar:
            read palabra

            sed -i "s/$palabra/*****/g" archivo3.txt
        ;;
        2)
            cat archivo3.txt
        ;;
        3)
            cp -f Ejercicio2.sh menu_copia.sh
        ;;
        4)
            echo Ingrese un mail
            read mail

            if [[ $mail == *@* && $mail == *.com ]]
            then
                echo mail válido
            else
                echo mail inválido
            fi
        ;;
        5)
            echo gracias por utilizar este programa
        ;;
        *)
            echo opcion inválida
    esac
    echo ''
done