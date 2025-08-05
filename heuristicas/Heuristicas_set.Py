from referencia import VACIO, BLANCO, NEGRO
import numpy as np

def evaluar_tablero(tablero, jugador_color):
    puntuacion = 0
    oponente_color = BLANCO if jugador_color == NEGRO else NEGRO
    tamanio = tablero.tamanio
    centro = tamanio // 2

    pesos = np.fromfunction(
        lambda i, j: tamanio - (abs(i - centro) + abs(j - centro)),
        (tamanio, tamanio),
        dtype=int
    )

    for fila in tablero.grid:
        puntuacion += evaluar_linea(fila, jugador_color, oponente_color)

    for col in zip(*tablero.grid):
        puntuacion += evaluar_linea(col, jugador_color, oponente_color)

    puntuacion += evaluar_diagonales(tablero.grid, jugador_color, oponente_color)

    for i in range(tamanio):
        for j in range(tamanio):
            if tablero.grid[i][j] == jugador_color:
                puntuacion += pesos[i, j]
            elif tablero.grid[i][j] == oponente_color:
                puntuacion -= pesos[i, j] // 2

    puntuacion -= penalizar_aislamiento(tablero.grid, jugador_color)

    return puntuacion

def evaluar_linea(linea, jugador_color, oponente_color):
    puntuacion = 0
    longitud = len(linea)
    VACIO_STR = str(VACIO)
    jugador_str = str(jugador_color)
    oponente_str = str(oponente_color)

    for size in [5, 6]:
        for i in range(longitud - size + 1):
            ventana = linea[i:i + size]
            ventana_str = ''.join(str(celda) for celda in ventana)

            if ventana_str.count(jugador_str) == 5:
                puntuacion += 100000
            elif ventana_str.count(jugador_str) == 4 and ventana_str.count(VACIO_STR) >= 1:
                puntuacion += 8000
            elif ventana_str.count(jugador_str) == 3 and ventana_str.count(VACIO_STR) >= 2:
                puntuacion += 500
            elif ventana_str.count(jugador_str) == 2 and ventana_str.count(VACIO_STR) >= 3:
                puntuacion += 100

            if f"{oponente_str * 4}{VACIO_STR}" in ventana_str or f"{VACIO_STR}{oponente_str * 4}" in ventana_str:
                puntuacion -= 120000
            elif ventana_str.count(oponente_str) == 5:
                puntuacion -= 150000

    return puntuacion


def evaluar_diagonales(matriz, jugador, oponente):
    puntuacion = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in range(filas - 4):
        for col in range(columnas - 4):
            diagonal = [matriz[fila + i][col + i] for i in range(5)]
            puntuacion += evaluar_linea(diagonal, jugador, oponente)

    for fila in range(4, filas):
        for col in range(columnas - 4):
            diagonal = [matriz[fila - i][col + i] for i in range(5)]
            puntuacion += evaluar_linea(diagonal, jugador, oponente)

    return puntuacion

def penalizar_aislamiento(grid, jugador):
    posiciones = [(i, j) for i in range(len(grid))
                         for j in range(len(grid[0]))
                         if grid[i][j] == jugador]
    if not posiciones:
        return 0

    cx = sum(x for x, _ in posiciones) / len(posiciones)
    cy = sum(y for _, y in posiciones) / len(posiciones)

    penalizacion = 0
    for x, y in posiciones:
        distancia = abs(x - cx) + abs(y - cy)
        if distancia > 6:
            penalizacion += 5 * (distancia - 6)

    return penalizacion

def evaluar_tablero_malo(tablero, jugador_color):
    puntuacion = 0
    oponente_color = '⚪' if jugador_color == '⚫' else '⚫'
    tamanio = tablero.tamanio

    for i in range(tamanio):
        for j in range(tamanio):
            if tablero.grid[i][j] == jugador_color:
                distancia_centro = abs(i - tamanio // 2) + abs(j - tamanio // 2)
                puntuacion += distancia_centro

    for fila in tablero.grid:
        puntuacion += evaluar_linea_mala(fila, jugador_color, oponente_color)
    for col in zip(*tablero.grid):
        puntuacion += evaluar_linea_mala(col, jugador_color, oponente_color)
    puntuacion += evaluar_diagonales_malas(tablero.grid, jugador_color, oponente_color)

    return puntuacion

def evaluar_linea_mala(linea, jugador, oponente):
    puntuacion = 0
    longitud = len(linea)

    jugador = str(jugador)
    oponente = str(oponente)
    VACIO_STR = str(VACIO)

    for i in range(longitud - 4):
        ventana = linea[i:i + 5]
        ventana_str = ''.join(str(celda) for celda in ventana)

        if ventana_str.count(oponente) == 4 and ventana_str.count(VACIO_STR) == 1:
            puntuacion += 1000
        if ventana_str.count(jugador) == 4 and ventana_str.count(VACIO_STR) == 1:
            puntuacion -= 500

    return puntuacion

def evaluar_diagonales_malas(matriz, jugador, oponente):
    puntuacion = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in range(filas - 4):
        for col in range(columnas - 4):
            diagonal = [matriz[fila + i][col + i] for i in range(5)]
            puntuacion += evaluar_linea_mala(diagonal, jugador, oponente)

    for fila in range(4, filas):
        for col in range(columnas - 4):
            diagonal = [matriz[fila - i][col + i] for i in range(5)]
            puntuacion += evaluar_linea_mala(diagonal, jugador, oponente)

    return puntuacion
