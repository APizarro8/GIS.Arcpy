# -*- coding: utf-8 -*-
#Propósito: Crear un script para presentarlo como herramienta en ArcGIS. 
#Autor: Alicia Pizarro
#Fecha: 25/01/2018

###########################################################################################################################
#IMPORTACIÓN DE LIBRERÍAS
import arcpy
import os
import time
import traceback

#Sobreescribir si es necesario
arcpy.env.overwriteOutput = True 

###########################################################################################################################
#Establecer el espacio de trabajo
arcpy.env.workspace = "D:\\Programacion\\Avanzada\\BCN_MADRID\\MADRID"

#Establecer directorios 
zona_estudio = os.path.join(arcpy.env.workspace, "Zona_estudio\\Municipios_estudio.shp")
salida = os.path.join(arcpy.env.workspace, "Resultados_ejer2")
if not os.path.exists(salida): #Si el directorio no existe, crealo.
    os.mkdir(salida)
    print "El directorio de salida ha sido creado"

#Listar capas entrada
Lista_capas_entrada = arcpy.ListFeatureClasses() #Listar las capas
    
#Abrir el archivo en modo escritura, que como no existe lo crea.
out_data = open ("D:\\Programacion\\Avanzada\\ListadoEntrada.txt", "w") 
for capa in Lista_capas_entrada:
    out_data.write(capa)
    out_data.write("\n")

out_data.close () #Cerrar el directorio de entrada

#Realizar acciones 
if Lista_capas_entrada:
    try:
        for capas in Lista_capas_entrada:
            descr = arcpy.Describe(capas) #Buscar las capas
            name = descr.name
            print "\n"
            print 'Nombre capa original: {0}'.format(name)
            
            nameClip = 'clip' + name
            print 'Nombre capa cortada: {0}'.format(nameClip)
            
            capa = os.path.join(salida, nameClip)
            
            arcpy.Clip_analysis(capas, zona_estudio, capa)
            print 'La capa {0} se ha cortado'.format(nameClip)
            
    except:
        arcpy.GetMessages()
        traceback.print_exc()
else:
    print "Las acciones no se han realizado"     

    
#Listar las capas de salida cortadas
arcpy.env.workspace = salida
Lista_capas_salida = arcpy.ListFeatureClasses()
   
#Abrimos el archivo en modo escritura, que como no existe lo crea.
out_data_clip = open ("D:\\Programacion\\Avanzada\\ListadoSalida.txt", "w") 
for capa in Lista_capas_salida:
    out_data_clip.write(capa)
    out_data_clip.write("\n")

out_data_clip.close () #Cerrar el listado de salida

print '=' * 50
print "\n"
 
###########################################################################################################################
#Tiempo de ejecución del proceso
tiempo_inicial = time.time() #Cuenta el tiempo de ejecución 
tiempo_final = time.time() # Cuenta el tiempo final de ejecución.
tiempo_empleado = tiempo_final - tiempo_inicial #Diferencia de tiempo de ejecución. 
print "El tiempo al comienzo ha sido de: ", tiempo_inicial, "segundos"
print "El tiempo al final ha sido de: ", tiempo_final, "segundos"
print "El programa ha tardado: ", tiempo_empleado, "segundos"
