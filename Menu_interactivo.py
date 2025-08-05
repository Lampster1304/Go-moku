# MenuInteractivo.py
import os
import msvcrt
from colorama import init, Fore, Style

init()

titulo = r"""



                                     ██████   ██████        ███    ███  ██████  ██   ██ ██    ██ 
                                    ██       ██    ██       ████  ████ ██    ██ ██  ██  ██    ██ 
                                    ██   ███ ██    ██ █████ ██ ████ ██ ██    ██ █████   ██    ██ 
                                    ██    ██ ██    ██       ██  ██  ██ ██    ██ ██  ██  ██    ██ 
                                     ██████   ██████        ██      ██  ██████  ██   ██  ██████ """

opciones = [
    "\n\n\n\n                                                        ·Humano vs Humano",
    "                                               ·Humano vs IA Minimax",
    "                                               ·IA Minimax vs IA Greedy",
    "                                               ·IA Minimax vs IA Mala",
    "                                               ·IA Minimax vs IA Random",
    "                                               ·IA Minimax vs IA Minimax",
    "                                               ·Salir"
]

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def leer_tecla():
    tecla = msvcrt.getch()
    if tecla == b'\x00' or tecla == b'\xe0':  # Teclas especiales (flechas)
        tecla2 = msvcrt.getch()
        teclas = {b'H': "UP", b'P': "DOWN"}
        return teclas.get(tecla2, None)
    elif tecla == b'\r':
        return "ENTER"
    return None

def mostrar_menu_interactivo():
    seleccion = 0
    ancho_centrado = 80
    while True:
        limpiar_pantalla()
        # Título en azul y centrado
        print("\n" + Fore.LIGHTBLUE_EX + titulo.center(ancho_centrado))

        for i, opcion in enumerate(opciones):
            if i == seleccion:
                # Seleccionado en verde brillante centrado
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"{opcion}".center(ancho_centrado) + Style.RESET_ALL)
            else:
                # Opciones normales en azul centrado
                print(Fore.LIGHTBLUE_EX + f"  {opcion}".center(ancho_centrado) + Style.RESET_ALL)

        print(Fore.LIGHTBLUE_EX + "\n\n\n\n                                     Usa las flechas ↑ ↓ para moverte y ENTER para seleccionar:\n".center(ancho_centrado))
        tecla = leer_tecla()
        if tecla == "UP":
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla == "DOWN":
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla == "ENTER":
            return seleccion + 1

# Solo se ejecuta si corres directamente este archivo
if __name__ == "__main__":
    mostrar_menu_interactivo()
