# -*- coding: utf-8 -*- 
#Propósito: Uso de módulos "arcpy" y "os" de la biblioteca estándar de Python para obtener un listado de archivos 
#creando sólo una copia de los archivos de tipo texto en otro directorio.  
#Autor: Alicia Pizarro
#Fecha: 27/10/2017

# IMPORTACIÓN DE MÓDULOS 
import arcpy
import os

## CREAR UNA LISTA PARA GUARDAR LOS DIRECCTORIOS 
lstArchivos = []

arcpy.env.workspace = 'xxDATAxx'
dirDest = 'xxDATAxx' #Variable para la ruta al directorio
lstArchivos = os.listdir(arcpy.env.workspace)        

for nomArch in lstArchivos:
    print (nomArch)

    if nomArch.endswith('txt'):
        nomArchDest = dirDest + nomArch[:-4] + 'V".txt'
        arcpy.Copy_management(nomArch, nomArchDest)
        print '{0} created.'.format(nomArchDest)
        
