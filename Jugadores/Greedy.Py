from referencia import NEGRO, BLANCO
from Tablero import Tablero
from heuristicas.Heuristicas_set import evaluar_tablero

class JugadorGreedy:
    def __init__(self, color, profundidad=1):
        self.color = color
        self.profundidad = profundidad
        self.oponente = BLANCO if color == NEGRO else NEGRO

    def obtener_movimiento(self, tablero: Tablero):
        print("IA Greedy (con heurística) está pensando...")
        mejor_valor = float('-inf')
        mejor_movimiento = None
        alfa = float('-inf')
        beta = float('inf')

        movimientos = tablero.obtener_movimientos_relevantes(radio=2)
        if not movimientos:
            movimientos = tablero.obtener_movimientos_validos()  # fallback si no hay movimientos cercanos

        for fila, col in movimientos:
            tablero.colocar(fila, col, self.color)
            valor = self.Greedy(tablero, self.profundidad - 1, False, alfa, beta)
            tablero.deshacer(fila, col)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = (fila, col)

            alfa = max(alfa, mejor_valor)

        print("Greedy eligió:", mejor_movimiento, "con puntuación:", mejor_valor)
        return mejor_movimiento


    def Greedy(self, tablero: Tablero, profundidad: int, es_maximizador: bool, alfa: float, beta: float) -> float:
        if tablero.verificar_ganador(self.color):
            return 1000000  # Muy alto si gana
        elif tablero.verificar_ganador(self.oponente):
            return -1000000  # Muy bajo si pierde
        elif profundidad == 0 or tablero.esta_lleno():
            return evaluar_tablero(tablero, self.color)

        if es_maximizador:
            max_eval = float('-inf')
            for fila, col in tablero.obtener_movimientos_relevantes(radio=2):
                tablero.colocar(fila, col, self.color)
                eval = self.Greedy(tablero, profundidad - 1, False, alfa, beta)
                tablero.deshacer(fila, col)

                max_eval = max(max_eval, eval)
                alfa = max(alfa, eval)
                if beta <= alfa:
                    break  # poda beta
            return max_eval
        else:
            min_eval = float('inf')
            for fila, col in tablero.obtener_movimientos_relevantes(radio=2):
                tablero.colocar(fila, col, self.oponente)
                eval = self.Greedy(tablero, profundidad - 1, True, alfa, beta)
                tablero.deshacer(fila, col)

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alfa:
                    break  # poda alfa
            return min_eval
