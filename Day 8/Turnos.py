def turnos_perfumeria():
    for n in range(1, 10000):
        yield "P - " + str(n)


def turnos_farmacia():
    turno = 1
    while True:
        yield "F - " + str(turno)
        turno += 1


def turnos_cosmeticos():
    turno = 1
    while True:
        yield "C - " + str(turno)
        turno += 1

p = turnos_perfumeria()
f = turnos_farmacia()
c = turnos_farmacia()

def decorador(funcion):
    print("\n" + "*" * 23)
    print("Su número es:")
    print(next(funcion))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")


