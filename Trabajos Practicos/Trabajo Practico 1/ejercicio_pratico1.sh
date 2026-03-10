#!/bin/bash

export FILENAME="archivo_final"
Ruta_Archivo_Consolidado="EPNro1/salida/$FILENAME.txt"

echo "
    Seleccione una opcion:
    1. - Crear entorno
    2. - Correr proceso
    3. - Ver archivo final
    4. - 
    5. - 
    6. - Salir
    "
read opc

until [[ $opc -eq 6 ]]
do
    case $opc in
    1) 
    #Crea el entorno si no existe
        if [[ -d "./EPNro1" ]]
        then
            echo -e "El entorno ya existe!\n"
        else
            echo procedemos con la creación del entorno . . .
            mkdir -p EPNro1/{entrada,salida,procesado}
        fi
        echo -e "\nEl entorno ha sido creado con exito!"
    ;;
    2)
    # Crea y corre el proceso de consolidación en background
        if [[ ! -f "./EPNro1/consolidar.sh" ]]; then

            echo creandos script de consolidación . . .

            touch EPNro1/consolidar.sh

            cat << EOF > EPNro1/consolidar.sh
#!/bin/bash

while true ; do    
    touch "EPNro1/salida/$FILENAME.txt"  
    for archivo in EPNro1/entrada/* ; do
        cat $archivo >> EPNro1/salida/$FILENAME.txt
        mv $archivo EPNro1/procesado/
    done
    sleep 60s
done
echo El script de consolidación se ha corrido con éxito!
EOF
                chmod +x ./EPNro1/consolidar.sh
        fi

        bash "./EPNro1/consolidar.sh &"
        pid=$(bash "./EPNro1/consolidar.sh &")
        echo Proceso iniciado en background . . .
    ;;
    3)
    # Ve el contenido del archivo consolidado
        if [[ -f $Ruta_Archivo_Consolidado ]]
        then
            sort -n $Ruta_Archivo_Consolidado
        else
            echo "No existe el archivo consolidado"
        fi
    ;;
    4)
        if [[ -f $Ruta_Archivo_Consolidado ]]
        then
            sort -n -k4 -r $Ruta_Archivo_Consolidado | head -n 5
        else
            echo "No existe el archivo consolidado"
        fi
    ;;
    5)
        echo "Ingresa un nro de padron para mostrar sus datos por pantalla"
        read alumno
        grep "$alumno" $Ruta_Archivo_Consolidado
    ;;
    6)
    # Sale del programa
    ;;
    esac

    echo " 
    Seleccione una opcion:
    1. - Crear entorno
    2. - Correr proceso
    3. - Ver archivo final
    4. - 
    5. - 
    6. - Salir
    "
    read opc
done

echo Saliendo . . .
pkill -f "./EPNro1dir/consolidar.sh"
rm -r "./EPNro1"