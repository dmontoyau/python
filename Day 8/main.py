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


if __name__ == "__main__":
    finalizar_programa = False
    while finalizar_programa == False:
        opcion = menu()
        if opcion == 1:
            t.decorador(opcion)
        elif opcion == 2:
            t.decorador(opcion)
        elif opcion == 3:
            t.decorador(opcion)
        elif opcion == 4:
            print("Hasta luego")
            finalizar_programa = True
        else:
            print("Opcion no valida")
