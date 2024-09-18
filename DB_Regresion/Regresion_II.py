# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:42:55 2022

@author: gmunaretti
"""

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


cnxn = pyodbc.connect(r'Driver=SQL Server;Server=EZESQL;Database=DW;Trusted_Connection=yes;')
cursor = cnxn.cursor()

try:
    SQL_Query = pd.read_sql_query(
        '''  SELECT     IdCertificacion,
            			FechaCertificacion  
  
  
            FROM [DW].[dbo].[F_GESTIONRAMPA]


            group by    IdCertificacion,
            			FechaCertificacion  

            order by 1
          ''', cnxn)

    df = pd.DataFrame(SQL_Query, columns=['IdCertificacion', 'FechaCertificacion'])
    print(df.head)
    print('The data type of df is: ', type(df))
except:
    print("Error: unable to convert the data")
    
df.head()

df.plot()



plt.show()
