class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    def __str__(self):
        cola = []
        act = self.frente

        while act:
            cola.append(act.dato)
            act = act.prox

        return f'{cola}'

    def encolar(self, dato):
        nuevo = _Nodo(dato, None)

        if self.frente is None:
            self.frente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo

    def desencolar(self):
        if self.frente is None:
            raise ValueError('La cola esta vacia')

        dato = self.frente.dato
        self.frente = self.frente.prox

        if self.frente is None:
            self.ultimo = None

        return dato
    
    def ver_frente(self):
        if self.frente is None:
            raise ValueError('La cola esta vacia')
        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None