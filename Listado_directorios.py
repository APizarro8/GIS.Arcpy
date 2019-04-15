# -*- coding: utf-8 -*- 
#Proposito: Crear un script para presentarlo como herramienta en ArcGIS. 
#Autor: Alicia Pizarro
#Fecha: 25/01/2018

#####################################################################################################################
##IMPORTACIÓN DE LIBRERÍAS 
import arcpy
import os

#Sobreescribir si es necesario
arcpy.env.overwriteOutput = True 

#####################################################################################################################
#Establecer directorio de trabajo
arcpy.env.workspace = "xxxDATAxxxx"
zona_Localiza = os.path.join(arcpy.env.workspace, "\\zona_Localiza.shp")
salida = os.path.join(arcpy.env.workspace, "Resultados_ejer2")
if not os.path.exists(salida): #Si el directorio no existe, crealo.
    os.mkdir(salida)
    print "El directorio {0} ha sido creado".format(salida)

#Listar capas entrada
Lista_capas_entrada = arcpy.ListFeatureClasses() #Listar las capas
print "La lista de las capas de entrada es:"
for capa in Lista_capas_entrada:
    print Lista_capas_entrada
    print '=' * 50
    
#Abrirmos el archivo en modo escritura, como no existe lo crea.
out_data = open ("\\ListadoEntrada.txt", "w") 
for capa in Lista_capas_entrada:
    out_data.write(capa)
    out_data.write("\n")

out_data.close () #Cerrar el archivo

#Espacio entre capa y capa
print "\n"

#Listar las capas de salida cortadas
arcpy.env.workspace = salida
Lista_capas_salida = arcpy.ListFeatureClasses()
print "La lista de capas de salida cortadas es:"
for capa in Lista_capas_salida:
    print Lista_capas_salida
    print '=' * 50

#Abrimos el archivo en modo escritura, que como no existe lo crea.
out_data_clip = open ("\\ListadoSalida.txt", "w") 
for capa in Lista_capas_salida:
    out_data_clip.write(capa)
    out_data_clip.write("\n")

out_data_clip.close () #Cerrar el archivo

###########################################################################################################################
#Tiempo de ejecución del proceso
tiempo_inicial = time.time() #Cuenta el tiempo de ejecución 
tiempo_final = time.time() # Cuenta el tiempo final de ejecución.
tiempo_empleado = tiempo_final - tiempo_inicial #Diferencia de tiempo de ejecución. 
print "El tiempo al comienzo ha sido de: ", tiempo_inicial, "segundos"
print "El tiempo al final ha sido de: ", tiempo_final, "segundos"
print "El programa ha tardado: ", tiempo_empleado, "segundos"

################################################# FINISH RUN #############################################################
#########################################################################################################################
