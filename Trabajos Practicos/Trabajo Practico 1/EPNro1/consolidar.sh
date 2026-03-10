#!/bin/bash

while true ; do    
    touch "EPNro1/salida/archivo_final.txt"  
    for archivo in EPNro1/entrada/* ; do
        cat  >> EPNro1/salida/archivo_final.txt
        mv  EPNro1/procesado/
    done
    sleep 60s
done
echo El script de consolidación se ha corrido con éxito!
