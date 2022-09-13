def run():
    edad = int(input("Cuanos anios tienes? "))

    if edad >= 18:
        tiene_licencia = int(input("""
        Tienes licencia?
        1. Si
        2. No
        """))
        if tiene_licencia == 1:
            print("puedes conducir excelente!!!!! ")
        else:
            print("Eres mayor de edad pero no tienes licencia nopuedes conducir")
    elif edad < 18:
        print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    else:
        print("Algo salio mal.....")


if __name__ == "__main__":
    run()