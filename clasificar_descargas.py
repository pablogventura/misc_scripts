#!/bin/python

import os
import re
import datetime

path_descargas = '/home/pablo/Descargas'

path_general = '/home/pablo/Escritorio/Completos'

ext_videos = ['mpg','mpeg','mp4','wmv','avi', 'flv']
path_videos = 'videos'

ext_musica = ['flac','mp3','wma','wav']
path_musica = 'musica'

ext_fotos = ['jpg','bmp']
path_fotos = 'fotos'

ext_windows = ['exe']
path_windows = 'windows'

ext_documentos = ['pdf','doc']
path_documentos = 'documentos'

ext_comprimidos = ['zip','rar','tgz','tar','gz','7z']
path_comprimidos = 'comprimidos'

ext_programas = ['deb','bin']
path_programas = 'programas'

ext_codigo = ['py','c']
path_codigo = 'codigo'

path_desconocidos = 'desconocidos'


def filtro(nombre):
    return os.path.isfile(nombre) and (len(nombre)<5 or nombre[-5:] != '.part')

def destinos(ext):
    if ext == 'otros':
        return path_general
    elif ext in ext_musica:
        return os.path.join(path_general,path_musica)
    elif ext in ext_videos:
        return os.path.join(path_general,path_videos)
    elif ext in ext_fotos:
        return os.path.join(path_general,path_fotos)
    elif ext in ext_windows:
        return os.path.join(path_general,path_windows)
    elif ext in ext_documentos:
        return os.path.join(path_general,path_documentos)
    elif ext in ext_comprimidos:
        return os.path.join(path_general,path_comprimidos)
    elif ext in ext_programas:
        return os.path.join(path_general,path_programas)
    elif ext in ext_codigo:
        return os.path.join(path_general,path_codigo)
    else:
        return os.path.join(path_general,path_desconocidos)

def clasif(nombre):
    match=re.search(r'\.(?P<extension>[^.]+)$',nombre)
    if match:
        extension = match.group('extension')
        return destinos(extension)
    else:
        return destinos('otros')

if not os.path.exists(path_general):
    os.mkdir(path_general)

if not os.path.exists(os.path.join(path_general,path_musica)):
    os.mkdir(os.path.join(path_general,path_musica))

if not os.path.exists(os.path.join(path_general,path_videos)):
    os.mkdir(os.path.join(path_general,path_videos))

if not os.path.exists(os.path.join(path_general,path_fotos)):
    os.mkdir(os.path.join(path_general,path_fotos))

if not os.path.exists(os.path.join(path_general,path_windows)):
    os.mkdir(os.path.join(path_general,path_windows))

if not os.path.exists(os.path.join(path_general,path_documentos)):
    os.mkdir(os.path.join(path_general,path_documentos))

if not os.path.exists(os.path.join(path_general,path_comprimidos)):
    os.mkdir(os.path.join(path_general,path_comprimidos))

if not os.path.exists(os.path.join(path_general,path_programas)):
    os.mkdir(os.path.join(path_general,path_programas))

if not os.path.exists(os.path.join(path_general,path_codigo)):
    os.mkdir(os.path.join(path_general,path_codigo))

if not os.path.exists(os.path.join(path_general,path_desconocidos)):
    os.mkdir(os.path.join(path_general,path_desconocidos))    

ficheros = filter(filtro, os.listdir(path_descargas))

for f in ficheros:

        ts = os.path.getmtime(os.path.join(path_descargas,f))
        fecha = datetime.date.fromtimestamp(ts)
        fecha = "%s-%s-%s" % (fecha.day, fecha.month, fecha.year)
        if not os.path.exists(os.path.join(clasif(f),fecha)):
            os.mkdir(os.path.join(clasif(f),fecha))
        os.symlink(os.path.join(path_descargas,f), os.path.join(os.path.join(clasif(f),fecha),f) )



