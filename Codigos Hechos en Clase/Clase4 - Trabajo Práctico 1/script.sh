#!/bin/bash

if [ "$1" == "-d" ]; then
    echo "Eliminando entorno y matando procesos..."

    # Eliminar la carpeta si existe
    [ -d EPNro1 ] && rm -r EPNro1

    # Matar procesos relacionados a consolidar.sh (si están corriendo)
    pkill -f consolidar.sh

    exit 0
fi

opc=0

FILENAME=archivo_consolidado.txt

while [ $opc -ne 6 ]
do 
    echo "Ingrese una opción:"
    echo "1. - Crear Entorno"
    echo "2. - Correr proceso"
    echo "3. - Mostrar listado"
    echo "4. - Mostrar las 10 notas más altas"
    echo "5. - Buscar estudiante"
    echo "6. - Salir"
    read opc
    case $opc in
    1)  
        if [ -d "EPNro1" ] ; then
            echo "El entorno ya está creado!"
        else
            echo "Se procede con la creación del entorno"
            mkdir EPNro1/entrada EPNro1/salida EPNro1/procesado 
        fi
    ;;
    2)
        if pgrep -f "consolidar.sh" > /dev/null ; then
            echo "El proceso se ya está corriendo en segundo plano!"
        else
            cat <<EOF > EPNro1/consolidar.sh
#!/bin/bash
FILENAME=\$1
while true; do
    for archivo in entrada/* ; do
        cat "\$archivo" >> EPNro1/salida/\$FILENAME.txt
        mv "\$archivo" EPNro1/procesado/
    done
    sleep 30
done
EOF
            bash EPNro1/consolidar.sh "$FILENAME" &
            echo "El proceso se ha lanzado en segundo plano."
        fi
        ;;
    3)
        if [ -f EPNro1/salida/$FILENAME ] ; then
            sort EPNro1/salida/$FILENAME
        else 
            echo "No existe el archivo $FILENAME! intenta primero corriendo el proceso."
        fi
    ;;
    4)
        if [ -f EPNro1/salida/$FILENAME ] ; then
            sort -k4 -n -r EPNro1/salida/$FILENAME | head -n 10
        else 
            echo "No existe el archivo $FILENAME! intenta primero corriendo el proceso."
        fi
    ;;
    5)
        echo "Ingresa el número de padrón del estudiante que deseas buscar:"
        read -r padron
        if [ -f EPNro1/salida/$FILENAME ] ; then
            grep "^$padron" EPNro1/salida/$FILENAME
        else 
            echo "No existe el archivo $FILENAME! intenta primero corriendo el proceso."
        fi
    ;;
    6)
    echo "Saliendo. . . "
    echo "Gracias por utilizar nuestro programa~"
    ;;
    *)
    echo "Opción inválida, por favor intente nuevamente"

    esac
done