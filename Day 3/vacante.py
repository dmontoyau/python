def run():
    habla_ingles = int(input("Sabes ingles?     1. Si     2. No  "))
    if habla_ingles == 1:
        habla_ingles = True
    else:
        habla_ingles = False

    sabe_python = int(input("Sabes python?    1. Si     2. No  " ))
    if sabe_python == 1:
        sabe_python = True
    else:
        sabe_python = False

    if habla_ingles and sabe_python:
        print("contratado")
    elif habla_ingles and sabe_python== False:
        print("necesitas saber python   ")
    elif habla_ingles == False and sabe_python:
        print("Necesitas tambien ingles   ")
    else:
        print("No eres apto para la oferta te falta todo.")


if __name__== "__main__":
    run()