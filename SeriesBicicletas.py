# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:11:30 2020

@author: gmunaretti
"""

import pandas as pd
from datetime import datetime

# Leer archivos de datos
viajes = pd.read_csv('2019-10.csv')

"""
Procesamiento
Para obtener la cantidad de viajes se puede incorporar un índice temporal al dataframe y
luego agrupar según la cantidad de viajes por hora. Concatenamos las columnas de fecha y
hora de retiro separadas por un espacio y cambiamos el tipo de dato de string a datetime.
Luego asignamos los tiempos al índice del dataframe y limpiamos posibles valores para otros meses o años.

"""


# concatenar Hora_Retiro y Fecha_Retiro
viajes['fecha_hora_retiro'] = viajes.Fecha_Retiro + ' ' + viajes.Hora_Retiro

# cambiar de str a datetime
viajes['fecha_hora'] = viajes.fecha_hora_retiro \
                             .map(lambda x : datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))

# reindexar el dataframe
viajes.index = viajes.fecha_hora

# limpiar valores de otros años
viajes = viajes.loc['2019-10']