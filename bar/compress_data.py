import shutil
import os 

shutil.make_archive('data/compress/resident-population', 'zip', 'data/descompress/resident-population')

if os.path.exists('data/compress/resident-population.zip'):
    print("-----Archivo creado correctamente-----")
else:
    ("Error al crear el archivo zip")