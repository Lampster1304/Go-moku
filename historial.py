from datetime import datetime
import os

def guardar_en_historial(ganador, color):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha_hora} | Ganador: {ganador} | Ficha: {color}\n"
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

def mostrar_historial():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\n                                   ========= HISTORIAL DE PARTIDAS =========\n")
                print(contenido)
            else:
                print("\nNo hay partidas registradas aún.\n")
    except FileNotFoundError:
        print("\nNo hay historial disponible.\n")
    
    input("\nPresiona ENTER para volver al menú...")
