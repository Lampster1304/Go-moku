from referencia import VACIO

def evaluar_tablero(tablero, jugador_color):
    puntuacion = 0
    oponente_color = '⚪' if jugador_color == '⚫' else '⚫'

    # Evaluar filas
    for fila in tablero.tablero:
        puntuacion += evaluar_linea(fila, jugador_color, oponente_color)

    # Evaluar columnas
    for col in zip(*tablero.tablero):
        puntuacion += evaluar_linea(col, jugador_color, oponente_color)

    # Evaluar diagonales
    puntuacion += evaluar_diagonales(tablero.tablero, jugador_color, oponente_color)

    return puntuacion

def evaluar_linea(linea, jugador, oponente):
    puntuacion = 0
    linea_str = ''.join(linea)

    patrones = [
        (jugador * 5, 100000),  # Victoria
        (jugador * 4 + VACIO, 1000),
        (VACIO + jugador * 4, 1000),
        (jugador * 3 + VACIO, 100),
        (VACIO + jugador * 3, 100),
        (jugador * 2 + VACIO, 10),
        (VACIO + jugador * 2, 10),

        (oponente * 5, -100000),  # Derrota
        (oponente * 4 + VACIO, -1000),
        (VACIO + oponente * 4, -1000),
        (oponente * 3 + VACIO, -100),
        (VACIO + oponente * 3, -100),
        (oponente * 2 + VACIO, -10),
        (VACIO + oponente * 2, -10),
    ]

    for patron, valor in patrones:
        puntuacion += linea_str.count(patron) * valor

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
