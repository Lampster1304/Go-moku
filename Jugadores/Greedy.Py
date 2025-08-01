from referencia import NEGRO, BLANCO
from Tablero import Tablero
import copy

class JugadorGreedy:
    def __init__(self, color, profundidad=2):
        self.color = color
        self.profundidad = profundidad
        self.oponente = BLANCO if color == NEGRO else NEGRO

    def obtener_mejor_movimiento(self, tablero: Tablero):
        print("Jugador Greedy está calculando movimiento...")

        mejor_valor = float('-inf')
        mejor_movimiento = None

        for fila, col in tablero.obtener_movimientos_validos():
            tablero_copia = copy.deepcopy(tablero)
            tablero_copia.colocar_piedra(fila, col, self.color)
            valor = self.evaluar_tablero(tablero_copia)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = (fila, col)

        print("Mejor movimiento elegido:", mejor_movimiento)
        return mejor_movimiento

    def evaluar_tablero(self, tablero: Tablero):
        # Implementar una evaluación simple del tablero
        return sum(1 for fila in tablero.tablero for celda in fila if celda == self.color)
        beta = float('inf')

        for fila, col in tablero.obtener_movimientos_validos():
            tablero_copia = copy.deepcopy(tablero)
            tablero_copia.colocar_piedra(fila, col, self.color)
            valor = self.minimax(tablero_copia, self.profundidad - 1, False, alfa, beta)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = (fila, col)

            alfa = max(alfa, mejor_valor)

        print("Mejor movimiento elegido:", mejor_movimiento)
        return mejor_movimiento

    def greedy(self, tablero, profundidad, es_maximizador, alfa, beta):
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
                valor = self.minimax(tablero_copia, profundidad - 1, False, alfa, beta)
                mejor_valor = max(mejor_valor, valor)
                alfa = max(alfa, valor)
                if beta <= alfa:
                    break  # Poda beta
            return mejor_valor
        else:
            mejor_valor = float('inf')
            for fila, col in tablero.obtener_movimientos_validos():
                tablero_copia = copy.deepcopy(tablero)
                tablero_copia.colocar_piedra(fila, col, self.oponente)
                valor = self.minimax(tablero_copia, profundidad - 1, True, alfa, beta)
                mejor_valor = min(mejor_valor, valor)
                beta = min(beta, valor)
                if beta <= alfa:
                    break  # Poda alfa
            return mejor_valor

    def obtener_movimiento(self, tablero: Tablero):
        return self.obtener_mejor_movimiento(tablero)
