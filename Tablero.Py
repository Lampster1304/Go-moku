# Tablero.py

import numpy as np
from referencia import VACIO, NEGRO, BLANCO, SIMBOLOS

class Tablero:
    def __init__(self, tamanio=15):
        self.tamanio = tamanio
        self.grid = np.full((tamanio, tamanio), VACIO)

    def colocar_piedra(self, fila, columna, jugador):
        if self.grid[fila, columna] == VACIO:
            self.grid[fila, columna] = jugador
            return True
        return False

    def obtener_movimientos_validos(self):
        return [(r, c) for r in range(self.tamanio) for c in range(self.tamanio) if self.grid[r, c] == VACIO]
    
    def obtener_movimientos_relevantes(self, radio=2):
        posiciones = []
        for r in range(self.tamanio):
            for c in range(self.tamanio):
                if self.grid[r, c] != VACIO:
                    for dr in range(-radio, radio + 1):
                        for dc in range(-radio, radio + 1):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < self.tamanio and 0 <= nc < self.tamanio:
                                if self.grid[nr, nc] == VACIO:
                                    posiciones.append((nr, nc))
        return list(set(posiciones))


    def esta_lleno(self):
        return not (self.grid == VACIO).any()

    def mostrar(self):
        print("\n    " + "".join(f"{i:2}" for i in range(self.tamanio)))
        for i, fila in enumerate(self.grid):
            fila_str = "".join(SIMBOLOS[c] for c in fila)
            print(f"{i:2} {fila_str}")
        print()


    def reiniciar(self):
        self.grid[:, :] = VACIO

    def verificar_ganador(self, jugador):
        direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for fila in range(self.tamanio):
            for col in range(self.tamanio):
                if self.grid[fila, col] != jugador:
                    continue
                for dr, dc in direcciones:
                    conteo = 0
                    for i in range(5):
                        r, c = fila + i * dr, col + i * dc
                        if 0 <= r < self.tamanio and 0 <= c < self.tamanio and self.grid[r, c] == jugador:
                            conteo += 1
                        else:
                            break
                    if conteo == 5:
                        return True
        return False

    def hay_ganador(self):
        return self.verificar_ganador(NEGRO) or self.verificar_ganador(BLANCO)

    def colocar(self, fila, col, jugador):
        self.grid[fila, col] = jugador

    def deshacer(self, fila, col):
        self.grid[fila, col] = VACIO

    def movimientos_legales(self):
        return self.obtener_movimientos_validos()
