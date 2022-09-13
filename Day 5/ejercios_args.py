def suma_cuadrados(*args):
    suma = 0

    for args in args:
        suma += args ** 2

    return suma


def numeros_persona (nombre, *args):
    suma = 0
    for args in args:
        suma +=  args
    print(f"{nombre}, la suma de todos tus numeros es de: {suma}")
    return  nombre, suma




if __name__ == "__main__":
    suma = suma_cuadrados(1,4,6)
    print(f"la suma es: {suma}")

    suma = numeros_persona("Daniel", 2,4,5,2)
    print(suma)
