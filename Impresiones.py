# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:20:50 2021

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



"""print(fichero)

f = open(fichero)
reader = csv.reader(f)
for row in reader:
      print(row)
      
"""

filename = "C:/Users/gmunaretti/Downloads/Informe De Impresion_ABRIL.csv"

"""
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=";",skiprows=5)
print(data.shape)
print(data)





with open(filename) as File:
    reader = csv.reader(File, delimiter=';', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
        
print(row['Nombre de Usuario'],row['Nombre Completo'])

"""
#******************************************************************************

df = pd.read_csv('C:/Users/gmunaretti/Downloads/Informe De Impresion_ABRIL.csv',encoding='latin-1', sep=';', skiprows=2)
df


df.head





















#*******************************************************************************
        
        
        
results = []
with open(filename) as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print(results)