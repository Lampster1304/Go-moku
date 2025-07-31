import msvcrt
import os
import time
import msvcrt
from referencia import VACIO, NEGRO, BLANCO, SIMBOLOS
from Tablero import Tablero

def leer_tecla():
    tecla = msvcrt.getch()
    if tecla == b'\x00':  # tecla especial flechas en tu caso
        tecla2 = msvcrt.getch()
        teclas = {b'H': "UP", b'P': "DOWN", b'K': "LEFT", b'M': "RIGHT"}
        return teclas.get(tecla2, None)
    elif tecla in [b' ', b'\r']:
        return "ENTER"
    elif tecla in [b'q', b'Q']:
        return "Q"
    else:
        return None

class Movimiento:
    def __init__(self):
        self.TAMANIO = 15
        self.tablero = Tablero(self.TAMANIO)
        self.cursor = [self.TAMANIO // 2, self.TAMANIO // 2]
        self.jugador_actual = NEGRO
        self.running = True

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_tablero(self):
        self.limpiar_pantalla()
        print("Usa flechas para mover cursor, espacio o enter para colocar pieza, Q para salir.")
        print(f"Turno de: {'⚫ Negro' if self.jugador_actual == NEGRO else '⚪ Blanco'}\n")

        for fila in range(self.TAMANIO):
            fila_str = ""
            for col in range(self.TAMANIO):
                if [fila, col] == self.cursor:
                    # Mostrar ficha del jugador en la posición del cursor
                    fila_str += f"{SIMBOLOS[self.jugador_actual]} "
                else:
                    fila_str += f"{SIMBOLOS[self.tablero.grid[fila, col]]} "
            print(fila_str)
        print()



    def mover_cursor(self, tecla):
        fila, col = self.cursor
        if tecla == "UP" and fila > 0:
            fila -= 1
        elif tecla == "DOWN" and fila < self.TAMANIO - 1:
            fila += 1
        elif tecla == "LEFT" and col > 0:
            col -= 1
        elif tecla == "RIGHT" and col < self.TAMANIO - 1:
            col += 1
        self.cursor = [fila, col]

    def colocar_pieza(self):
        fila, col = self.cursor
        if self.tablero.colocar_piedra(fila, col, self.jugador_actual):
            if self.tablero.verificar_ganador(self.jugador_actual):
                self.mostrar_tablero()
                ganador = "⚫ Negro" if self.jugador_actual == NEGRO else "⚪ Blanco"
                print(f"¡{ganador} gana!")
                self.running = False
            elif self.tablero.esta_lleno():
                self.mostrar_tablero()
                print("¡Empate! El tablero está lleno y no hay ganador.")
                self.running = False
            else:
                self.jugador_actual = BLANCO if self.jugador_actual == NEGRO else NEGRO
        else:
            print("Casilla ocupada, elige otra posición.")
            time.sleep(1)


    def leer_tecla(self):
        tecla = msvcrt.getch()
        if tecla == b'\x00':  # tecla especial flechas para ti
            tecla2 = msvcrt.getch()
            teclas = {b'H': "UP", b'P': "DOWN", b'K': "LEFT", b'M': "RIGHT"}
            return teclas.get(tecla2, None)
        elif tecla in [b' ', b'\r']:
            return "ENTER"
        elif tecla in [b'q', b'Q']:
            return "Q"
        else:
            return None

    def jugar(self):
        while self.running:
            self.mostrar_tablero()
            tecla = self.leer_tecla()
            if tecla in ["UP", "DOWN", "LEFT", "RIGHT"]:
                self.mover_cursor(tecla)
            elif tecla == "ENTER":
                self.colocar_pieza()
            elif tecla == "Q":
                print("Juego terminado por el usuario.")
                self.running = False

if __name__ == "__main__":
    juego = Movimiento()
    juego.jugar()