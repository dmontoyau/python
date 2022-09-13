def run():
    texto = input("""
    Hola!
    por favor ingresa un texto o frase
    """).lower()

    letra1= input("Ingrese una letra ").lower()
    print(f"La letra ingresada esta:  {texto.count(letra1)} veces en el texto")
    letra2 = input("Ingrese una letra ").lower()
    print(f"La letra ingresada esta:  {texto.count(letra2)} veces en el texto")
    letra3 = input("Ingrese una letra ").lower()
    print(f"La letra ingresada esta:  {texto.count(letra3)} veces en el texto")
    print("")

    print(f"La primera detra del texto es: {texto[0]} y la ultima letra es: {texto[-1]}")

    palabras = texto.split()
    print(f"La cantidad de palabras es: {len(palabras)}")

    palabras.reverse()
    invertido = " ".join(palabras)
    print(f"tu texto invertido es: {invertido} ")


    # print(texto.find("python"))
    #
    # hola = bool(texto.find("python"))
    # if hola == True:
    #     print("estaaaa")
    # else:
    #     print("no esta")

    buscar_python = 'python' in texto
    dic = {True: "si", False: "no"}
    print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")

if __name__ == "__main__":
    run()