from referencia import VACIO

def evaluar_tablero(tablero, jugador_color):
    puntuacion = 0
    oponente_color = '⚪' if jugador_color == '⚫' else '⚫'

    # Evaluar filas
    for fila in tablero.grid:
        puntuacion += evaluar_linea(fila, jugador_color, oponente_color)

    # Evaluar columnas
    for col in zip(*tablero.grid):
        puntuacion += evaluar_linea(col, jugador_color, oponente_color)

    # Evaluar diagonales
    puntuacion += evaluar_diagonales(tablero.grid, jugador_color, oponente_color)

    return puntuacion

def evaluar_linea(linea, jugador, oponente):
    puntuacion = 0
    longitud = len(linea)

    jugador = str(jugador)
    oponente = str(oponente)
    VACIO_STR = str(VACIO)

    for i in range(longitud - 4):
        ventana = linea[i:i + 5]
        ventana_str = ''.join(str(celda) for celda in ventana)

        # Ataque (jugador)
        if ventana_str.count(jugador) == 5:
            puntuacion += 100000
        elif ventana_str.count(jugador) == 4 and ventana_str.count(VACIO_STR) == 1:
            puntuacion += 5000
        elif ventana_str.count(jugador) == 3 and ventana_str.count(VACIO_STR) == 2:
            puntuacion += 300
        elif ventana_str.count(jugador) == 2 and ventana_str.count(VACIO_STR) == 3:
            puntuacion += 30

        # Defensa (oponente)
        if ventana_str.count(oponente) == 5:
            puntuacion -= 100000
        elif ventana_str.count(oponente) == 4 and ventana_str.count(VACIO_STR) == 1:
            puntuacion -= 90000  # Muy alta para obligar a defender
        elif ventana_str.count(oponente) == 3 and ventana_str.count(VACIO_STR) == 2:
            puntuacion -= 500
        elif ventana_str.count(oponente) == 2 and ventana_str.count(VACIO_STR) == 3:
            puntuacion -= 50

    return puntuacion

def evaluar_diagonales(matriz, jugador, oponente):
    puntuacion = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    # Diagonales descendentes ↘
    for fila in range(filas - 4):
        for col in range(columnas - 4):
            diagonal = [matriz[fila + i][col + i] for i in range(5)]
            puntuacion += evaluar_linea(diagonal, jugador, oponente)

    # Diagonales ascendentes ↗
    for fila in range(4, filas):
        for col in range(columnas - 4):
            diagonal = [matriz[fila - i][col + i] for i in range(5)]
            puntuacion += evaluar_linea(diagonal, jugador, oponente)

    return puntuacion
