from referencia import NEGRO, BLANCO
from Tablero import Tablero
import msvcrt

class Humano:
    def __init__(self, color):
        self.color = color
        self.cursor = [7, 7] 

    def leer_tecla(self):
        tecla = msvcrt.getch()
        if tecla == b'\x00':
            tecla2 = msvcrt.getch()
            teclas = {b'H': "UP", b'P': "DOWN", b'K': "LEFT", b'M': "RIGHT"}
            return teclas.get(tecla2, None)
        elif tecla in [b' ', b'\r']:
            return "ENTER"
        elif tecla in [b'q', b'Q']:
            return "Q"
        else:
            return None

    def mover_cursor(self, direccion, tamanio):
        fila, col = self.cursor
        if direccion == "UP" and fila > 0:
            fila -= 1
        elif direccion == "DOWN" and fila < tamanio - 1:
            fila += 1
        elif direccion == "LEFT" and col > 0:
            col -= 1
        elif direccion == "RIGHT" and col < tamanio - 1:
            col += 1
        self.cursor = [fila, col]

    def obtener_movimiento(self, tablero: Tablero):
        while True:
            tecla = self.leer_tecla()
            if tecla in ["UP", "DOWN", "LEFT", "RIGHT"]:
                self.mover_cursor(tecla, tablero.tamanio)
            elif tecla == "ENTER":
                fila, col = self.cursor
                if tablero.grid[fila, col] == 0:
                    return fila, col
                else:
                    print("Casilla ocupada. Intenta otra.")
            elif tecla == "Q":
                print("Saliendo...")
                return None
