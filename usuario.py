# ➤ Importaciones

from comandos import *

# ➤ Constantes

# Comandos
IR = 'ir'
ITINERARIO = 'itinerario'
VIAJE = 'viaje'
REDUCIR_CAMINOS = 'reducir_caminos'
COMANDOS = (IR, ITINERARIO, VIAJE, REDUCIR_CAMINOS)

# Errores
ERROR_COMANDO = 'Error: Comando incorrecto'

def comandos(cmd, sedes_no_dirigido, coordenadas, sedes):

    # Condiciones de programa dependiendo de la entrada ingresada
    if cmd[0] == IR and len(cmd) == 4:
        return ir(cmd, sedes_no_dirigido, coordenadas, sedes)

    if cmd[0] == ITINERARIO and len(cmd) == 2:
        return itinerario(cmd, sedes_no_dirigido)

    if cmd[0] == VIAJE and len(cmd) == 3:
        return viaje(cmd, sedes_no_dirigido, coordenadas, sedes)

    if cmd[0] == REDUCIR_CAMINOS and len(cmd) == 2:
        return reducir_caminos(cmd, sedes_no_dirigido, coordenadas)

    if cmd[0] not in COMANDOS:
        return f'{ERROR_COMANDO}' # Error cuando ingresa un comando invalido