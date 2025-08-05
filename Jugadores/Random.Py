import random
from referencia import VACIO

class JugadorRandom:
    def __init__(self, color):
        self.color = color

    def obtener_movimiento(self, tablero):
        movimientos_validos = self.obtener_movimientos_validos(tablero)
        if not movimientos_validos:
            return None
        return random.choice(movimientos_validos)

    def obtener_movimientos_validos(self, tablero):
        movimientos = []
        for fila in range(tablero.tamanio):
            for columna in range(tablero.tamanio):
                if tablero.grid[fila][columna] == VACIO:
                    movimientos.append((fila, columna))
        return movimientos
