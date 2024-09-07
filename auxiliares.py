# ➤ Importaciones

from grafo import Grafo
from biblioteca import *

# Recibe la ruta de un archivo. Devuelve True si existe, False en caso contrario
def existe_archivo(ruta):
    try:
        with open(ruta) as f:
            return True
    except FileNotFoundError as e:
        return False

# Recibe la ruta del pajek y carga la informacion del mismo. Devuelve un grafo no dirigido con las conexiones de
# todas las sedes y un diccionario que contiene las coordenadas de todas las sedes
def cargar_pajek(ruta_pajek):
    sedes_no_dirigido = Grafo(False) 
    coordenadas = {}

    with open(ruta_pajek) as f:

        ciudades = int(f.readline())

        for i in range(ciudades):
            linea = f.readline().rstrip().split(",")
            sedes_no_dirigido.agregar_vertice(linea[0])
            coordenadas[linea[0]] = (linea[1], linea[2])

        conexiones = int(f.readline())

        for i in range(conexiones):
            linea = f.readline().rstrip().split(",")
            sedes_no_dirigido.agregar_arista(linea[0], linea[1], int(linea[2]))

        return sedes_no_dirigido, coordenadas

# Recibe la ruta de las recomendaciones y un grafo no dirigido que contiene las sedes. Agrega las conexiones
# correspondientes de las sedes en un grafo dirigido segun el archivo de recomendaciones
def cargar_recomendaciones(ruta_recomendaciones, sedes_no_dirigido):
    sedes_dirigido = Grafo(True)

    with open(ruta_recomendaciones) as f:
        for linea in f:
            linea = linea.rstrip().split(',')
            sedes_dirigido.agregar_vertice(linea[0])
            orden = bfs(sedes_no_dirigido, linea[0])

            if linea[1] not in orden:
                return

            sedes_dirigido.agregar_vertice(linea[1])
            sedes_dirigido.agregar_arista(linea[0], linea[1])
  
    return sedes_dirigido

# Recibe un recorrido, las coordenadas y el nombre del archivo. Crea un archivo kml con la informacion del recorrido
def escribir_kml(camino, coordenadas, nombre_archivo):
    visitados = set()

    with open(nombre_archivo, 'w') as w:
        w.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
        w.write(f'<kml xmlns="http://earth.google.com/kml/2.1">\n')
        w.write(f'\t<Document>\n')
        w.write(f'\t\t<name>Camino desde {camino[0]} hacia {camino[-1]}</name>\n')

        w.write('\n')

        for sede in camino:
            if sede not in visitados:
                w.write(f'\t\t<Placemark>\n')
                w.write(f'\t\t\t<name>{sede}</name>\n')
                w.write(f'\t\t\t<Point>\n')
                w.write(f'\t\t\t\t<coordinates>{coordenadas[sede][0]}, {coordenadas[sede][1]}</coordinates>\n')
                w.write(f'\t\t\t</Point>\n')
                w.write(f'\t\t</Placemark>\n')
                visitados.add(sede)

        w.write('\n')

        for i in range(len(camino) - 1):
            w.write(f'\t\t<Placemark>\n')
            w.write(f'\t\t\t<LineString>\n')
            w.write(f'\t\t\t\t<coordinates>{coordenadas[camino[i]][0]}, {coordenadas[camino[i]][1]} {coordenadas[camino[i + 1]][0]}, {coordenadas[camino[i + 1]][1]}</coordinates>\n')
            w.write(f'\t\t\t</LineString>\n')
            w.write(f'\t\t</Placemark>\n')
            
        w.write(f'\t</Document>\n')
        w.write(f'</kml>\n')

# Recibe el recorrido, las coordenadas y el nombre del archivo. Crea un archivo pajek con la informacion del recorrido
def escribir_pajek(camino, coordenadas, nombre_archivo):
    aristas = obtener_aristas(camino)

    with open(nombre_archivo, 'w') as w:
        w.write(f'{len(coordenadas)}\n')

        for sede in coordenadas:
            coordenada = coordenadas[sede]
            latitud, longitud = coordenada[0], coordenada[1]
            w.write(f'{sede},{latitud},{longitud}\n')

        w.write(f'{len(aristas)}\n')

        for origen, destino, peso in aristas:
            w.write(f'{origen},{destino},{peso}\n')