# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:07:47 2021

@author: gmunaretti
"""

#==============================================================================
#=  FUNCIONA CORRECTAMENTE                                                    =
#==============================================================================

import pymssql  
 

 
try:
    conn = pymssql.connect(server='EZESQL', user='prueba2', password='21', database='ModeloDeNegocio') 
    print("\n"*5)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
    
    
cursor = conn.cursor()  
cursor.execute('SELECT * FROM ModeloDeNegocio.dbo.MOD_Habilitaciones;') 
row = cursor.fetchone()  

while row:  
      print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) )    
      row = cursor.fetchone()  