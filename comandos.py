# ➤ Importaciones

from auxiliares import *
from biblioteca import *

# ➤ Constantes

FLECHA = ' -> '
TIEMPO_TOTAL = 'Tiempo total: '
PESO_TOTAL = 'Peso total: '

ERROR_RECORRIDO = 'No se encontro recorrido'
ERROR_ARCHIVO = 'Error: Lectura de archivos'

def ir(cmd, sedes_no_dirigido, coordenadas, sedes):
    desde, hasta = cmd[1], cmd[2]

    # Error si no existe recorrido posible
    if desde not in sedes or hasta not in sedes:
        return f'{ERROR_RECORRIDO}'

    # Obtenemos el recorrido minimo y el tiempo que se tarda
    camino, tiempo = reconstruir_camino_minimo(sedes_no_dirigido, desde, hasta)

    # Error si no existe recorrido
    if not camino:
        return f'{ERROR_RECORRIDO}'

    # Escribimos la informacion del recorrido en un archivo kml
    escribir_kml(camino, coordenadas, cmd[3])
   
    # Obtenemos el recorrido minimo desde un lugar a otro y cuanto tarda
    return f'{FLECHA.join(camino)}\n{TIEMPO_TOTAL}{tiempo}'

def itinerario(cmd, sedes_no_dirigido):
    
    # Error si no existe un archivo de recomendaciones
    if not existe_archivo(cmd[1]):
        return f'{ERROR_ARCHIVO}'

    # Cargamos la informacion de las recomendaciones en un grafo auxiliar
    sedes_dirigido = cargar_recomendaciones(cmd[1], sedes_no_dirigido)

    # Agregamos las sedes faltantes al grafo auxiliar
    for v in sedes_no_dirigido.obtener_vertices():
        if v not in sedes_dirigido.obtener_vertices():
            sedes_dirigido.agregar_vertice(v)

    # Obtenemos el recorrido recomendado
    camino = camino_topologico(sedes_dirigido)

    # Error si no existe recorrido
    if not camino:
        return f'{ERROR_RECORRIDO}'

    # Obtenemos el recorrido recomendado
    return f'{FLECHA.join(camino)}'
    
def viaje(cmd, sedes_no_dirigido, coordenadas, sedes):

    # Error si no existe el origen ingresado
    if not cmd[1] in sedes:
        return f'{ERROR_RECORRIDO}'

    # Obtenemos el recorrido desde el origen haciendo un tour por todas las sedes
    camino = hierholzer(sedes_no_dirigido, cmd[1])

    # Error si no existe recorrido
    if not camino:
        return f'{ERROR_RECORRIDO}'

    # Obtenemos el tiempo que se tarda en recorrer todo el tour
    tiempo = calcular_peso(sedes_no_dirigido, camino)

    # Escribimos la informacion del recorrido en un archivo kml
    escribir_kml(camino, coordenadas, cmd[2])

    # Obtenemos el tour completo y cuanto tarda
    return f'{FLECHA.join(camino)}\n{TIEMPO_TOTAL}{tiempo}'

def reducir_caminos(cmd, sedes_no_dirigido, coordenadas):

    # Obtenemos el recorrido con menor tiempo para recorrer todas las sedes
    camino, tiempo = mst_kruskal(sedes_no_dirigido)

    # Escribimos la informacion obtenida en un archivo pajek
    escribir_pajek(camino, coordenadas, cmd[1])

    # Obtenemos el tiempo que se tarda
    return f'{PESO_TOTAL}{tiempo}'