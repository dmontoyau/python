import Turnos as t


def menu():
    finalizar = False

    while finalizar == False:
        try:
            opcion = int(input("""Bienvenido a la Farmacia
            A que area desea acercarse?
            [1] Perfumeria
            [2] Farmacia
            [3] Cosmeticos
            [4] Salir
            """))
            if opcion not in range(0, 5):
                finalizar = False
                print("El numero de opcion elegido no es valido. ")
            else:
                finalizar = True
                return opcion
        except:
            print("No ha ingresado una opcion valida, intentelo de nuevo")


def decora_funcion(funcion):
    print("Hola buen dia, su turno es: ")
    print(next(funcion))
    print("Aguarde y sera atendido \n")


if __name__ == "__main__":
    finalizar_programa = False
    while finalizar_programa == False:
        opcion = menu()
        if opcion == 1:
            perfume = t.turnos_perfumeria()
            #decora_funcion(perfume)
            t.decorador(perfume)
        elif opcion == 2:
            farmacia = t.turnos_farmacia()
            decora_funcion(farmacia)
        elif opcion == 3:
            cosmetico = t.turnos_cosmeticos()
            decora_funcion(cosmetico)
        elif opcion == 4:
            print("Hasta luego")
            finalizar_programa = True
        else:
            print("Opcion no valida")
