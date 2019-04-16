# -*- coding: utf-8 -*-
#Ejercicio 3 practica 1. 
#Propósito: La finalidad de esta práctica ha sido desarrollar un script que crease una herramienta para ArcGIS que localizase
#una zona en concreto, donde las diferentes variables de entrada se han recortado corforme a la capa de entrada, 
#luego se ha realizado un buffer sobre ellas, se disuelva y se unan en una única zona.   
#Autor: Alicia Pizarro
#Fecha: 01/02/2018

############################################################################################################################
#IMPORTAR MODULOS DE ARCPY
import os
import arcpy

#SOBREESCRIBIR EN CASO DE QUE YA EXISTA
arcpy.env.overwriteOutput = True

############################################################################################################################
#ESTABLECER EL ESPACIO DE TRABAJO
##ENTRADA DE VARIABLES 
arcpy.env.workspace = arcpy.GetParameterAsText(0)
nucleo = os.path.join(arcpy.GetParameterAsText(1))
distancia_nucleo = arcpy.GetParameterAsText(2)
autovia = os.path.join(arcpy.GetParameterAsText(3))
autopista = os.path.join(arcpy.GetParameterAsText(4))
distancia_carretera = arcpy.GetParameterAsText(5)
salida = arcpy.GetParameterAsText(6)

municipios = os.path.join(arcpy.env.workspace, "xxDATAxxENTRADAxx.shp")
zona_estudio = os.path.join(salida, "xxxDATAxxSALIDAxx.shp")

#Obtener la zona de estudio eliminando aquellos registros que se correspondan con municipios cuyo campo 'Zona' sea: 
#Municipio de Madrid o Norte Metropolitano o Este Metropolitano o Sur Metropolitano u Oeste Metropolitano.
#Crear un cursor que actualiza las filas Municipios apuntando al campo 'Zona'.
municipioUp = arcpy.UpdateCursor(municipios, '', '', 'Zona') 

try:
    for municipios_row in municipioUp:
        zona_row = municipios_row.getValue('Zona') #Obtener el valor del campo 'Zona'
        if zona_row == "Nordeste Comunidad" or zona_row == "Sierra Central" or zona_row == "Sierra Norte" or zona_row ==
        "Sierra Sur" or zona_row == "Sudeste Comunidad" or zona_row == "Sudoeste Comunidad":
            municipioUp.deleteRow(municipios_row) #Eliminar aquellos registros que no pertenecen a los registros de interes.
        
    zona_estudio = os.path.join(salida, "xxxDATAxxSALIDAxx.shp") #Creacion del limite de la capa de estudio
    arcpy.Copy_management(municipios, zona_estudio)
    print 'La capa sobre la zona de estudio ha sido creada como: "xxxDATAxxSALIDAxx".'
    print '=' * 50

except:
    print "EL cursor de actualizacion no se ha ejecutado"    
    
try:
    autovias_recorte = os.path.join(salida, "Autovias_recorte.shp")
    arcpy.Clip_analysis(autovia, zona_estudio, autovias_recorte)
    
    autopistas_recorte = os.path.join(salida, "Autopistas_recorte.shp")
    arcpy.Clip_analysis(autopista, zona_estudio, autopistas_recorte)
    
    nucleo_recorte = os.path.join(salida, "Nucleo_recorte.shp")
    arcpy.Clip_analysis(nucleo, zona_estudio, nucleo_recorte)   
        
    autovias_buffer = os.path.join(salida, "Autovias_buffer.shp")
    arcpy.Buffer_analysis(autovias_recorte, autovias_buffer, distancia_carretera, "FULL", "ROUND", "ALL", "#")
    
    autopistas_buffer = os.path.join(salida, "Autopistas_buffer.shp")
    arcpy.Buffer_analysis(autopistas_recorte, autopistas_buffer, distancia_carretera, "FULL", "ROUND", "ALL", "#")
    
    nucleo_buffer = os.path.join(salida, "Nucleo_buffer.shp")
    arcpy.Buffer_analysis(nucleo_recorte, nucleo_buffer, distancia_nucleo, "FULL", "ROUND", "ALL", "#")    
    
    merge_buffer = os.path.join(salida, "Merge_buffer.shp")
    arcpy.Merge_management([autovias_buffer, autopistas_buffer, nucleo_buffer], merge_buffer)
    
    dissolve_buffer = os.path.join(salida, "Dissolve_buffer.shp")
    arcpy.Dissolve_management(merge_buffer, dissolve_buffer, "#", "#", "MULTI_PART", "DISSOLVE_LINES")
    
    arcpy.AddField_management(dissolve_buffer, "excluir", "LONG", 2, "", field_is_nullable="NULLABLE")
    arcpy.CalculateField_management(dissolve_buffer, "excluir", "1", "")    
    
    zona_estudio_merge = os.path.join(salida, "Zona_estudio_merge.shp")
    arcpy.Union_analysis(in_features=[dissolve_buffer, zona_estudio], out_feature_class=zona_estudio_merge, join_attributes="ALL")
    
    localiza = os.path.join(salida, "zona_localiza.shp")
    arcpy.Select_analysis(in_features=zona_estudio_merge, out_feature_class=localiza, where_clause='excluir <> 1')
    
except:
    print "No se ha podido realizar la accion"
    
#################################################### FINISH RUN ############################################################
############################################################################################################################
