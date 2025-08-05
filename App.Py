from Movimiento import Movimiento
from Jugadores.Humano import Humano
from Jugadores.Minimax import JugadorMinimax
from Jugadores.Greedy import JugadorGreedy
from Jugadores.Mala import JugadorMalo
from Jugadores.Random import JugadorRandom
from Menu_interactivo import mostrar_menu_interactivo

def ejecutar_modo(modo):
    if modo == 1:
        juego = Movimiento(modo="HH")
    elif modo == 2:
        juego = Movimiento(modo="HI")
    elif modo == 3:
        juego = Movimiento(modo="II_MINIMAX_GREEDY")
    elif modo == 4:
        juego = Movimiento(modo="II_MINIMAX_MALA")
    elif modo == 5:
        juego = Movimiento(modo="II_MINIMAX_RANDOM")
    elif modo == 6:
        juego = Movimiento(modo="II_MINIMAX_MINIMAX")
    else:
        print("Saliendo del juego...")
        return

    juego.jugar()

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu_interactivo()
        if opcion == 7:  # Salir
            print("\nGracias por jugar. ¡Hasta la próxima!\n")
            break
        ejecutar_modo(opcion)

