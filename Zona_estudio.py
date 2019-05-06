# -*- coding: utf-8 -*-
#Proposito:  A partir de la capa Municipios.shp obtener la zona de estudio pedida, Zona_estudio, creando un cursor de 
#actualización con la condición de que deben eliminarse todos los registros en el que el campo “zona” no sea Municipio de 
#Madrid o Norte Metropolitano o Este Metropolitano o Sur Metropolitano u Oeste Metropolitano.
#Autor: Alicia Pizarro
#Fecha: 29/01/2018

#############################################################################################################################
#IMPORTACIÓN DE MÓDULOS
import os
import arcpy
import traceback
import time

#SOBREESCRIBIR EL ARCHIVO EN CASO DE QUE EXISTA 
arcpy.env.overwriteOutput = True

#############################################################################################################################
#ESTABLECER ESPACIO DE TRABAJO 
entrada = "xxxDATAxxENTRADAxxx"
salida = os.path.join(entrada,"xxDATAxxSALIDAxx")
if not os.path.exists(salida): #Si el directorio no existe, lo crea.
    os.mkdir(salida)

#Variable de entrada sobre la cuál se obtiene la zona de estudio
municipio = os.path.join(entrada,"xxCAPAxxRECORTE.shp")

#Obtener la zona de estudio eliminando aquellos registros que se correspondan con municipios cuyo campo 'Zona' sea:
#Municipio de Madrid o Norte Metropolitano o Este Metropolitano o Sur Metropolitano u Oeste Metropolitano.
#Crear un cursor que actualiza las filas Municipios apuntando al campo 'Zona'.
municipioUp = arcpy.UpdateCursor(municipio, '', '', 'Zona') 

try:
    for municipio_row in municipioUp:
        zona_row = municipio_row.getValue('Zona') #Obtener el valor del campo 'Zona'
        if zona_row == "Nordeste Comunidad" or zona_row == "Sierra Central" or zona_row == "Sierra Norte" or zona_row ==
        "Sierra Sur" or zona_row == "Sudeste Comunidad" or zona_row == "Sudoeste Comunidad":
            municipioUp.deleteRow(municipio_row) #Eliminar aquellos registros que no pertenecen a los registros de interes.
        
    zona_estudio = os.path.join(salida, "xxxDATAxxx.shp") #Creacion del limite de la capa de estudio
    arcpy.Copy_management(municipio, zona_estudio)
    print 'La capa sobre la zona de estudio ha sido creada como: "xxxDATAxxx".'
    print '=' * 50

##############################################################################################################################
#GESTIÓN DE ERRORES  
except:
    arcpy.GetMessages()
    traceback.print_exc()
    
#TIEMPO DE EJECUCIÓN DEL PROCESO
tiempo_inicial = time.time() #Cuenta el tiempo de ejecución 
tiempo_final = time.time() # Cuenta el tiempo final de ejecución.
tiempo_empleado = tiempo_final - tiempo_inicial #Diferencia de tiempo de ejecución. 
print "El tiempo al comienzo ha sido de: ", tiempo_inicial, "segundos"
print "El tiempo al final ha sido de: ", tiempo_final, "segundos"
print "El programa ha tardado: ", tiempo_empleado, "segundos"

####################################################### FINISH RUN ###########################################################
##############################################################################################################################
