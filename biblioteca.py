# ➤ Importaciones

from cola import Cola
from grafo import Grafo
from pila import Pila
from union_find import UnionFind
from heapq import *

# ➤ Biblioteca con funciones genericas de grafos

def grados(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = 0
        for w in grafo.adyacentes(v):
            grados[v] += 1
    return grados

def entradas(grafo):
    entradas = {}
    for v in grafo.obtener_vertices():
        entradas[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            entradas[w] += 1
    return entradas

def cantidad_grados_impar(grafo):
    g = grados(grafo)
    grados_impares = 0
    for v in grafo.obtener_vertices():
        if g[v] % 2 != 0:
            grados_impares += 1
    return grados_impares

def bfs(grafo, origen): 
    orden = {}
    visitados = set()
    cola = Cola()
    
    orden[origen] = 0
    visitados.add(origen)
    cola.encolar(origen)

    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = orden[v] + 1
                visitados.add(w)
                cola.encolar(w)

    return orden

def es_conexo(grafo):
    origen = grafo.vertice_aleatorio()
    visitados = set()
    cola = Cola()

    visitados.add(origen)
    cola.encolar(origen)

    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.encolar(w)

    return len(visitados) == len(grafo.obtener_vertices())

def calcular_peso(grafo, camino):
    peso = 0
    for i in range(len(camino) - 1):
        peso += grafo.peso_arista(camino[i], camino[i + 1])
    return peso

def camino_minimo_dijkstra(grafo, origen):
    distancias = {}  
    padres = {}

    for v in grafo.obtener_vertices():
        distancias[v] = float("inf")
        
    distancias[origen] = 0
    padres[origen] = None

    heap = []
    heappush(heap, (origen, 0)) 
    
    while len(heap) != 0:
        v, _ = heappop(heap)
        for w in grafo.adyacentes(v):
            distancia_por_aca = distancias[v] + grafo.peso_arista(v, w)
            if distancia_por_aca < distancias[w]:
                distancias[w] = distancia_por_aca
                padres[w] = v
                heappush(heap, (w, distancias[w]))

    return distancias, padres

def reconstruir_camino_minimo(grafo, desde, hasta):
    camino = [hasta]
    distancias, padres = camino_minimo_dijkstra(grafo, desde)
    
    if distancias[hasta] == float('inf'): 
        return None, None

    v = padres[hasta]
    while v != desde:
        camino.append(v)
        v = padres[v]

    camino.append(desde)
    return camino[::-1], distancias[hasta]

def pila_a_lista(pila):
    lista = []
    while not pila.esta_vacia():
        lista.append(pila.desapilar())
    return lista

def camino_topologico_dfs(grafo, v, visitados, pila):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            camino_topologico_dfs(grafo, w, visitados, pila)
        
    pila.apilar(v)

def camino_topologico(grafo):
    visitados = set()
    pila = Pila()

    for v in grafo.obtener_vertices():
        if v not in visitados:
            visitados.add(v)
            camino_topologico_dfs(grafo, v, visitados, pila)

    return pila_a_lista(pila)

def obtener_aristas(grafo):
    aristas = []
    visitados = set()

    for v in grafo.obtener_vertices():
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if w not in visitados:
                aristas.append((v, w, grafo.peso_arista(v,w)))

    return aristas

def mst_kruskal(grafo):
    conjuntos = UnionFind(grafo.obtener_vertices())
    aristas = sorted(obtener_aristas(grafo), key=lambda arista: arista[2])
    arbol = Grafo(False, grafo.obtener_vertices())
    peso_arbol = 0

    for arista in aristas:
        v, w, peso = arista

        if conjuntos.find(v) == conjuntos.find(w):
            continue

        arbol.agregar_arista(v, w, peso)
        peso_arbol += peso
        conjuntos.union(v, w)
        
    return arbol, peso_arbol

def tiene_ciclo_euleriano(grafo):
    return es_conexo(grafo) and cantidad_grados_impar(grafo) == 0

def dfs_hierholzer(grafo, v, visitados, camino):
    for w in grafo.adyacentes(v):
        if (v, w) not in visitados:
            visitados.add((v, w))
            visitados.add((w, v))
            dfs_hierholzer(grafo, w, visitados, camino)

    camino.append(v)

def hierholzer(grafo, origen):
    if not tiene_ciclo_euleriano(grafo):
        return None

    visitados = set()
    camino = []
    dfs_hierholzer(grafo, origen, visitados, camino)
    return camino