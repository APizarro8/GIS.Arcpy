# -*- coding: utf-8 -*-
#Ejercicio 2 practica 1. 
#Proposito: Crear un script para presentarlo como herramienta en ArcGIS. 
#Autor: Alicia Pizarro
#Fecha: 25/01/2018

import arcpy
import os

#Sobreescribir si es necesario
arcpy.env.overwriteOutput = True 

#Establecer los par�metros de entrada de la herramienta
arcpy.env.workspace = arcpy.GetParameterAsText(0) #Directorio donde se guardan las capas del BCN #Directorio donde se guardan las capas del BCN
zona_estudio = arcpy.GetParameterAsText(1) #Capa limite de zona de estudio
salida = arcpy.GetParameterAsText(2) #Directorio de salida 
Lista_entrada = arcpy.GetParameterAsText(3) #Archivo de texto donde se guardarán los datos del directorio de entrada
Lista_salida = arcpy.GetParameterAsText(4) #Archivo de texto donde se guardarán los datos del directorio de salida

#Listar capas entrada
Lista_entrada = arcpy.ListFeatureClasses() #Listar las capas

    
#Abrirmos el archivo en modo escritura, que como no existe lo crea.
entrada = open ("D:\\Programacion\\Avanzada\\ListadoEntrada.txt", "w") 
for capa in Lista_entrada:
    entrada.write(capa)
    entrada.write("\n")

entrada.close () #Cerrar el directorio de entrada

#Realizar acciones 
if Lista_entrada:
    try:
        for capas in Lista_entrada:
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
else:
    print "Las acciones no se han realizado"     


#Listar las capas de salida cortadas
arcpy.env.workspace = salida
Lista_salida = arcpy.ListFeatureClasses()

#Abrimos el archivo en modo escritura, que como no existe lo crea.
salida = open ("D:\\Programacion\\Avanzada\\ListadoSalida.txt", "w") 
for capa in Lista_salida:
    salida.write(capa)
    salida.write("\n")

salida.close () #Cerrar el directorio de salida
