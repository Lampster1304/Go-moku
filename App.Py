from Movimiento import Movimiento
from Menu_interactivo import mostrar_menu_interactivo
from historial import mostrar_historial

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
        if opcion == 8: 
            print("\nGracias por jugar. ¡Hasta la próxima!\n")
            break
        elif opcion == 7:
            mostrar_historial()
        else:
            ejecutar_modo(opcion)