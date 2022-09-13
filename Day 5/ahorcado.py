from random import *


def elegir_palabra(lista_palabras):
    palabra_elegia = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegia))

    return palabra_elegia, letras_unicas


def pedir_letra():
    letra_elegida = ""
    es_valida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")

    print(" ".join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra. Intenta una nueva. ")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era: " + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("FELICITACIONES HAS ENCONTRADO LA PALABRA!!!!!")

    return True


if __name__ == "__main__":

    palabras = ["navidad", "ganar", "reto"]

    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    aciertos = 0
    juego_terminado = False

    palabra, letras_unicas = elegir_palabra(palabras)

    while not juego_terminado:
        print("\n" + "*" * 20 + "\n")
        mostrar_nuevo_tablero(palabra)
        print("\n")
        print("Letras incorrectas: " + "-".join(letras_incorrectas))
        print(f"Te quedas {intentos} vidas.")
        print("\n" + "*" * 20 + "\n")

        letra = pedir_letra()

        intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

        juego_terminado = terminado