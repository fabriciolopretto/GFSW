#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importamos las librerías necesarias
import requests
import os
import glob
import datetime

time = datetime.datetime.utcnow()
año_real = int(time.year)
mes_real = int(time.month)
dia_real = int(time.day)

# Introducimos la corrida del modelo
#año
año_tex = str(año_real)
#mes
if 10 > mes_real >= 1:
    mes_tex = '0' + str(mes_real)
if mes_real >= 10:
    mes_tex = str(mes_real)
#dia
if 10 > dia_real >= 1:
    dia_tex = '0' + str(dia_real)
if dia_real >= 10:
    dia_tex = str(dia_real)

del time,año_real,mes_real,dia_real

# Generamos la ruta de descarga
path_script = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(path_script)

# Limpiamos la carpeta de destino de corridas anteriores
files = glob.glob(ruta + '/Archivo de hielo/*.grib2')
for f in files:
    os.remove(f)
del files,f

# Creamos el camino de los archivos
# Descarga todas las variables del modelo global
downloadURL = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/seaice_analysis/prod/seaice_analysis.'+ año_tex + mes_tex + dia_tex +'/'+'seaice.t00z.5min.grb.grib2'
# Descarga todas las variables del HN 
req = requests.get(downloadURL)
filename = req.url[downloadURL.rfind('/')+1:]
# Descargamos el archivo vigente
with open(ruta + '/Archivo de hielo/'+ filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
del downloadURL,req,filename,chunk
