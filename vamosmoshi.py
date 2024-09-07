#!/usr/bin/python3

# ➤ Importaciones

from auxiliares import *
from biblioteca import *
from usuario import *
import sys

sys.setrecursionlimit(10000)

# ➤ Constantes

MAX_PARAMETROS_REQUERIDOS = 2

# Errores
ERROR_PARAMETROS = 'Error: Faltan parámetros'

def main():

    # Variables a utilizar
    args = sys.argv

    # Error si no hay suficientes parametros ingresados
    if len(args) < MAX_PARAMETROS_REQUERIDOS:
        return f'{ERROR_PARAMETROS}'

    # Cargamos la informacion del pajek
    sedes_no_dirigido, coordenadas = cargar_pajek(args[1])
    sedes = sedes_no_dirigido.obtener_vertices()

    # Pedimos entradas al usuario
    while True:
      
        # Entrada del usuario
        try:
            entrada = input().split(", ")
        except EOFError:
            break
        
        # Separamos la entrada
        cmd = [entrada[0].split()[0]] + [' '.join(entrada[0].split()[1:])] + entrada[1:]
        
        # Acciones dependiendo del comando ingresado por el usuario
        print(comandos(cmd, sedes_no_dirigido, coordenadas, sedes))
        
main()