# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:47:19 2021

@author: gmunaretti
"""

import os
import csv
import numpy
import pandas as pd

ejemplo_dir = 'C:/Users/gmunaretti/Downloads'

with os.scandir(ejemplo_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.csv')]

for fichero in ficheros:
    print(fichero) 



filename = "C:/Users/gmunaretti/Downloads/IMP-2019-09-27.csv"

df = pd.read_csv(filename,encoding='latin-1', sep=';', skiprows=2)
df

df.head

# Se toma solo un fichero de la lista ficheros
fich = ficheros[0]

ExtraerFecha = fich[4:14]

print(ExtraerFecha)

#df['Fecha'] = ExtraerFecha

df.insert(0,'Fecha',ExtraerFecha)

df.info()

df.columns

df.columns[2]

df.head(7)

df['Nombre de Usuario'].is_unique