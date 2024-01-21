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
hora_real = int(time.hour)

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
#inicio   
if 0 <= hora_real < 12:
    hora_tex = '00'
if 12 <= hora_real <= 23:
   hora_tex = '12'

del time,año_real,mes_real,dia_real,hora_real

# Generamos la ruta de descarga
path_script = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(path_script)

# Limpiamos la carpeta de destino de corridas anteriores
files = glob.glob(ruta + '/Archivos/*.grib2')
for f in files:
    os.remove(f)
del files,f

# Creamos el camino de los archivos
for i in range(79):
    if 10 > i >= 0:
        plazo = '00' + str(i)
    if 100 > i >= 10:
        plazo = '0' + str(i)
    if i >= 100:
        plazo = str(i)   
    #Descarga todas las variables del modelo global
    downloadURL = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.'+ año_tex + mes_tex + dia_tex +'/'+ hora_tex + '/wave/gridded/gfswave.t'+ hora_tex +'z.global.0p25.f'+ plazo +'.grib2'
    #Descarga todas las variables globales 
    req = requests.get(downloadURL)
    filename = req.url[downloadURL.rfind('/')+1:]
    #Descargamos el archivo vigente
    with open(ruta + '/Archivos/'+ filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    del plazo,downloadURL,req,filename,chunk
