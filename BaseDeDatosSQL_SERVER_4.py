# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:59:04 2021

@author: gmunaretti
"""
import pymssql


def get_conn(self):
        """
        Returns a mssql connection object
        """
        conn = self.get_connection(self.mssql_conn_id)  # pylint: disable=no-member
        # pylint: disable=c-extension-no-member
        conn = pymssql.connect(
            server='EZESQL/ddd',
            user='prueba2',
            password='10',
            database='ModeloDeNegocio'
           
        )
        return conn 
  

try:
      Conexion = get_conn
      print("\n"*5)
      print('Conexion exitosa')

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
    
    
    
    
