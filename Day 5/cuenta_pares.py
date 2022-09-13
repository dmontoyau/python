def cuenta_pares(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma = suma + i
    print(f"El total de la suma de la lista de pares es: {suma}")

if __name__ == "__main__":
    lista = [3,4,6,7,9,11,34]
    cuenta_pares(lista)