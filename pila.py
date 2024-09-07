class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.tope = None
    
    def apilar(self, dato):
        nuevo = _Nodo(dato, self.tope)
        self.tope = nuevo

    def desapilar(self):
        if self.tope is None:
            raise ValueError('La pila esta vacia')

        dato = self.tope.dato
        self.tope = self.tope.prox

        return dato

    def ver_tope(self):
        if self.tope is None:
            raise ValueError('La pila esta vacia')
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None