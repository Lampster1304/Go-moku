from Movimiento import Movimiento
from referencia import VACIO
from heuristicas.Heuristicas_set import evaluar_tablero_malo
import copy

class JugadorMalo:
    def __init__(self, color):
        self.color = color

    def obtener_movimiento(self, tablero):
        movimientos_validos = self.obtener_movimientos_validos(tablero)
        peor_movimiento = None
        peor_puntuacion = float('-inf')

        for fila, columna in movimientos_validos:
            copia_tablero = copy.deepcopy(tablero)
            copia_tablero.colocar_piedra(fila, columna, self.color)
            puntuacion = evaluar_tablero_malo(copia_tablero, self.color)

            if puntuacion > peor_puntuacion:
                peor_puntuacion = puntuacion
                peor_movimiento = (fila, columna) 

        return peor_movimiento

    def obtener_movimientos_validos(self, tablero):
        movimientos = []
        for fila in range(tablero.tamanio):
            for columna in range(tablero.tamanio):
                if tablero.grid[fila][columna] == VACIO:
                    movimientos.append((fila, columna))
        return movimientos

