import random

class Grafo:
    def __init__(self, dirigido, lista_vertices = None):
        self.grafo = {}
        self.dirigido = dirigido

        if lista_vertices is not None:
            for v in lista_vertices:
                self.agregar_vertice(v)
  
    def agregar_vertice(self, v):
        if v not in self.grafo: 
            self.grafo[v] = {}

    def borrar_vertice(self, v):
        if v not in self.grafo: 
            return

        for w in self.grafo.keys():
            if w != v and v in self.grafo[w]: 
                self.grafo[w].pop(v)

        self.grafo.pop(v)

    def agregar_arista(self, v, w, peso = 1):
        if v not in self.grafo or w not in self.grafo: 
            return

        self.grafo[v][w] = (v, w, peso)

        if not self.dirigido: 
            self.grafo[w][v] = (w, v, peso)

    def borrar_arista(self, v, w):
        if v not in self.grafo or w not in self.grafo: 
            return

        if w in self.grafo[v]:
            if not self.dirigido:   
                self.grafo[w].pop(v)
            return self.grafo[v].pop(w)

    def estan_unidos(self, v, w):
        return False if v not in self.grafo else w in self.grafo[v]

    def peso_arista(self, v, w):
        return None if not self.estan_unidos(v, w) else self.grafo[v][w][2]

    def obtener_vertices(self):
        return [v for v in self.grafo]

    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())

    def adyacentes(self, v):
        return [w for w in self.grafo[v].keys()]

    def __str__(self):
        grafo = "\n"
        for v, w in self.grafo.items():
            grafo += str(v) + " " + str(w) + "\n"
        return f'{grafo}'