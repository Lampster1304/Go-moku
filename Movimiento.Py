import msvcrt
import os
import time
from referencia import VACIO, NEGRO, BLANCO, SIMBOLOS
from Tablero import Tablero

class Movimiento:
    def __init__(self, modo="HH"):
        self.TAMANIO = 15
        self.tablero = Tablero(self.TAMANIO)
        self.cursor = [self.TAMANIO // 2, self.TAMANIO // 2]
        self.jugador_actual = NEGRO
        self.running = True
        self.modo = modo
        self.jugador1 = None
        self.jugador2 = None

        if self.modo == "HH":
            from Jugadores.Humano import Humano
            self.jugador1 = Humano(NEGRO)
            self.jugador2 = Humano(BLANCO)

        elif self.modo == "HI":
            from Jugadores.Humano import Humano
            from Jugadores.Minimax import JugadorMinimax
            self.jugador1 = Humano(NEGRO)
            self.jugador2 = JugadorMinimax(BLANCO)
        
        elif self.modo == "II_MINIMAX_GREEDY":
            from Jugadores.Minimax import JugadorMinimax
            from Jugadores.Greedy import JugadorGreedy
            self.jugador1 = JugadorGreedy(NEGRO)
            self.jugador2 = JugadorMinimax(BLANCO)

        elif self.modo == "II_MINIMAX_MALA":
            from Jugadores.Minimax import JugadorMinimax
            from Jugadores.Mala import JugadorMalo
            self.jugador1 = JugadorMalo(NEGRO)
            self.jugador2 = JugadorMinimax(BLANCO)

        elif self.modo == "II_MINIMAX_RANDOM":
            from Jugadores.Minimax import JugadorMinimax
            from Jugadores.Random import JugadorRandom
            self.jugador1 = JugadorRandom(NEGRO)
            self.jugador2 = JugadorMinimax(BLANCO)

        elif self.modo == "II_MINIMAX_MINIMAX":
            from Jugadores.Minimax import JugadorMinimax
            self.jugador1 = JugadorMinimax(NEGRO)
            self.jugador2 = JugadorMinimax(BLANCO)

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_tablero(self):
        self.limpiar_pantalla()
        print("Usa flechas para mover cursor, espacio o enter para colocar pieza, Q para salir.")
        print(f"Turno de: {'⚪ Blanco' if self.jugador_actual == NEGRO else '⚫ Negro'}\n")

        for fila in range(self.TAMANIO):
            fila_str = ""
            for col in range(self.TAMANIO):
                if [fila, col] == self.cursor:
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

    def leer_tecla(self):
        tecla = msvcrt.getch()
        if tecla == b'\x00':  # Teclas especiales
            tecla2 = msvcrt.getch()
            teclas = {b'H': "UP", b'P': "DOWN", b'K': "LEFT", b'M': "RIGHT"}
            return teclas.get(tecla2, None)
        elif tecla in [b' ', b'\r']:
            return "ENTER"
        elif tecla in [b'q', b'Q']:
            return "Q"
        else:
            return None

    def colocar_pieza_humano(self):
        fila, col = self.cursor
        if self.tablero.colocar_piedra(fila, col, self.jugador_actual):
            return self.verificar_estado_post_movimiento()
        else:
            print("Casilla ocupada, elige otra posición.")
            time.sleep(1)
        return False

    def colocar_pieza_ia(self, movimiento):
        fila, col = movimiento
        if self.tablero.colocar_piedra(fila, col, self.jugador_actual):
            return self.verificar_estado_post_movimiento()
        else:
            print("Movimiento inválido.")
            time.sleep(1)
        return False

    def verificar_estado_post_movimiento(self):
        if self.tablero.verificar_ganador(self.jugador_actual):
            self.mostrar_tablero()
            ganador = "⚪ Blanco" if self.jugador_actual == NEGRO else "⚫ Negro"
            print(f"¡{ganador} gana!")
            self.running = False
        elif self.tablero.esta_lleno():
            self.mostrar_tablero()
            print("¡Empate! El tablero está lleno.")
            self.running = False
        else:
            self.jugador_actual = BLANCO if self.jugador_actual == NEGRO else NEGRO
        return True

    def jugar(self):
        while self.running:
            self.mostrar_tablero()
            jugador = self.jugador1 if self.jugador_actual == NEGRO else self.jugador2

            if jugador.__class__.__name__ == "Humano":
                tecla = self.leer_tecla()
                if tecla in ["UP", "DOWN", "LEFT", "RIGHT"]:
                    self.mover_cursor(tecla)
                elif tecla == "ENTER":
                    self.colocar_pieza_humano()
                elif tecla == "Q":
                    print("Juego terminado por el jugador.")
                    break
            else:
                movimiento = jugador.obtener_movimiento(self.tablero)
                if movimiento is None:
                    print("IA terminó el juego.")
                    break
                self.colocar_pieza_ia(movimiento)
