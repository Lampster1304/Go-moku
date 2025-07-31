from referencia import NEGRO, BLANCO
from Tablero import Tablero
import copy

class JugadorMinimax:
    def __init__(self, color, profundidad=2):
        self.color = color
        self.profundidad = profundidad
        self.oponente = BLANCO if color == NEGRO else NEGRO

    def obtener_mejor_movimiento(self, tablero: Tablero):
        mejor_valor = float('-inf')
        mejor_movimiento = None

        for fila, col in tablero.obtener_movimientos_validos():
            tablero_copia = copy.deepcopy(tablero)
            tablero_copia.colocar_piedra(fila, col, self.color)
            valor = self.minimax(tablero_copia, self.profundidad -1, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = (fila, col)

        return mejor_movimiento

    def minimax(self, tablero, profundidad, es_maximizador):
        if tablero.verificar_ganador(self.color):
            return 10
        elif tablero.verificar_ganador(self.oponente):
            return -10
        elif tablero.esta_lleno() or profundidad == 0:
            return 0

        if es_maximizador:
            mejor_valor = float('-inf')
            for fila, col in tablero.obtener_movimientos_validos():
                tablero_copia = copy.deepcopy(tablero)
                tablero_copia.colocar_piedra(fila, col, self.color)
                valor = self.minimax(tablero_copia, profundidad - 1, False)
                mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            mejor_valor = float('inf')
            for fila, col in tablero.obtener_movimientos_validos():
                tablero_copia = copy.deepcopy(tablero)
                tablero_copia.colocar_piedra(fila, col, self.oponente)
                valor = self.minimax(tablero_copia, profundidad - 1, True)
                mejor_valor = min(mejor_valor, valor)
            return mejor_valor
