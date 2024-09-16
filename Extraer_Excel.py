# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:21:13 2022

@author: gmunaretti
"""


import pandas as pd 
  
df = pd.read_excel('T:/Aplicaciones/Mantenimiento/Inspeccion50hs.xlsx', sheet_name = 'hoja1') 
df1 = pd.read_excel('T:/Aplicaciones/Mantenimiento/Inspeccion500hs.xlsx', sheet_name = 'hoja1')
df2 = pd.read_excel('T:/Aplicaciones/Mantenimiento/InspeccionDiaria742hs.xlsx', sheet_name = 'hoja1')
df3 = pd.read_excel('T:/Aplicaciones/Mantenimiento/Inspeccion250hs.xlsx', sheet_name = 'hoja1')




df.head()


