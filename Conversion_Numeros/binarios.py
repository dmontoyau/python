def binarios (numero):
    binario = []
    while numero > 1:
        binario.append(int(numero % 2))
        numero = numero / 2

    return binario[::-1]


def base_8(numero):
    base = []
    while numero > 1:
        base.append(int(numero % 8))
        numero = numero / 8

    return base[::-1]


def base_16(numero):
    dic = {}
    base = []
    while numero > 1:
        base.append(int(numero % 16))
        numero = numero / 16

    return base[::-1]



def base_5 (numero):
    base = []
    while numero > 1:
        base.append(int(numero % 5))
        numero = numero / 5

    print("l".join(base))


    #return fin


if __name__ == "__main__":
    print("""
    Esta calculadora te ayudara a convertir nuemro en base 10 a base 2(binarios).
    """)

    numero = int(input("Ingresa un numero para convertir: "))
    #print(base_5(numero))
    base_5(numero)