from Movimiento import Movimiento
from Jugadores.Humano import Humano
from Jugadores.Minimax import JugadorMinimax
# Puedes importar más IAs después aquí...

def mostrar_menu():
    print("🧠🎮 Bienvenido a Go-Moku 🎮🧠")
    print("Selecciona un modo de juego:")
    print("1. Humano vs Humano")
    print("2. Humano vs IA Minimax")
    print("3. IA Minimax vs IA Greedy")
    print("4. IA Minimax vs IA Mala")
    print("5. IA Minimax vs IA Random")
    print("6. Salir")

def ejecutar_modo(modo):
    if modo == "1":
        juego = Movimiento(modo="HH")
        juego.jugar()
    elif modo == "2":
        juego = Movimiento(modo="HI")
        juego.jugar()
    elif modo == "3":
        juego = Movimiento(modo="II_MINIMAX_GREEDY")
        juego.jugar()
    elif modo == "4":
        juego = Movimiento(modo="II_MINIMAX_MALA")
        juego.jugar()
    elif modo == "5":
        juego = Movimiento(modo="II_MINIMAX_RANDOM")
        juego.jugar()
    else:
        print("Saliendo del juego...")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")
        if opcion == "6":
            break
        ejecutar_modo(opcion)
