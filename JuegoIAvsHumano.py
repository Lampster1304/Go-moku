# JuegoIAvsHumano.py
from Tablero import Tablero
from referencia import NEGRO, BLANCO, SIMBOLOS
from Minimax import JugadorMinimax
from Humano import Humano
import os
import time

class JuegoIAvsHumano:
    def __init__(self):
        self.TAMANIO = 15
        self.tablero = Tablero(self.TAMANIO)
        self.ia = JugadorMinimax(NEGRO)
        self.humano = Humano(BLANCO)
        self.turno_actual = NEGRO
        self.running = True

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_tablero(self):
        self.limpiar_pantalla()
        print(f"Turno de: {'⚫ IA (Minimax)' if self.turno_actual == NEGRO else '⚪ Humano'}\n")
        for fila in range(self.TAMANIO):
            fila_str = ""
            for col in range(self.TAMANIO):
                if self.turno_actual == BLANCO and [fila, col] == self.humano.cursor:
                    fila_str += f"{SIMBOLOS[self.turno_actual]} "
                else:
                    fila_str += f"{SIMBOLOS[self.tablero.grid[fila, col]]} "
            print(fila_str)
        print()

    def jugar(self):
        while self.running:
            self.mostrar_tablero()

            if self.turno_actual == NEGRO:
                fila, col = self.ia.obtener_mejor_movimiento(self.tablero)
                time.sleep(1)
            else:
                movimiento = self.humano.obtener_movimiento(self.tablero)
                if movimiento is None:
                    print("El jugador humano ha salido.")
                    return
                fila, col = movimiento

            if self.tablero.colocar_piedra(fila, col, self.turno_actual):
                if self.tablero.verificar_ganador(self.turno_actual):
                    self.mostrar_tablero()
                    print(f"¡{'IA' if self.turno_actual == NEGRO else 'Humano'} gana!")
                    break
                elif self.tablero.esta_lleno():
                    self.mostrar_tablero()
                    print("¡Empate!")
                    break
                self.turno_actual = BLANCO if self.turno_actual == NEGRO else NEGRO
            else:
                print("Casilla ocupada.")
                time.sleep(1)
