# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:56:45 2021

@author: Gaston Munaretti
"""

import pyodbc 

direccion_servidor = 'EZESQL.intercargo.com.ar'
nombre_bd = 'ModeloDeNegocio'
nombre_usuario = 'prueba2'
password = '10'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
    
    
cursor = conexion.cursor()  
cursor.execute('SELECT * FROM ModeloDeNegocio.dbo.MOD_Habilitaciones;')  
    
#ODBC Driver 17 for 