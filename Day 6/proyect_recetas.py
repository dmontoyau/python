from pathlib import *
from os import system
import os


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def menu_opciones():
    system("cls")
    print("*" * 50)
    print("""  Buen dia bienvenido al restaurante""")
    print("*" * 50 + "\n")
    ruta = Path("C", "Usuarios", "Daniel Montoya", "Escritorio", "Python3", "Day 6", "Recetas")
    print("\n" + f"Las recetas disponibles estan en: \n{ruta}""")
    print(f"Total recetas: {contar_recetas(ruta)}""")
    menu = int(input(""" \nESTE ES EL MENU Y ESTAS SON LAS OPCIONES QUE TIENES DISPONIBLES.
    1. 
    2. 
    3. 
    4.
    5.
    """))




if __name__ == "__main__":
    menu = 0
    menu = menu_opciones()
    if menu == 1:
        pass
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        pass
    elif menu == 5:
        pass



