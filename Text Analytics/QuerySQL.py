# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:57:46 2020

@author: gmunaretti
"""

import pyodbc
import nltk


# Generar conexion con la base de datos
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ezesql;'
                          'Database=OPERACIONES;'
                          'Trusted_Connection=yes;')

# Definir un cursor
cur = conn.cursor()


# Definir consulta SQL
querystring = "SELECT  A.[diagnostico] FROM [OPERACIONES].[RrHh].[MedicinaLab_Cab] as A WHERE A.fecha > '2018-01-01'"


# Ejecutar consulta
cur.execute(querystring)

# Generar lista con los datos de la consulta
tabla =  cur.fetchall()

# recorrer lista pàra verificar
for r in tabla:
    print( r)
    
# Cerrar la conexion    
conn.close()


"""##########################################################################"""

# Tokenización de palabras
palabras_total=len(tabla)
print(palabras_total)


tokens_conjunto=set(tabla.Row)
palabras_diferentes=len(tokens_conjunto)
print(palabras_diferentes)