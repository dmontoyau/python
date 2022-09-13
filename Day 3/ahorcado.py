import random

numero = random.randint(1,5)
vidas = 8

while vidas >= 1:
    num = int(input("INGRESA UN NUMERO "))
    if num not in(range(1,100)):
        print("no valido")
    elif numero > num:
        print("Ingresa otro numero  mayor al que ingresaste")
    elif numero < num:
        print("Ingresa otro numero menor al que ingresaste")
    else:
        print("Ganaste")
        break

    vidas= vidas -1
    if vidas > 0:
        print(f"te quedan {vidas} vidas")
    else:
        print("Perdiste todos los intentos")

