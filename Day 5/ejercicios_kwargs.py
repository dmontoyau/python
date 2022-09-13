def cantidad_atributos(*args, **kwargs):
    cantidad = 0
    for args in args:
        cantidad += 1

    for kwargs in kwargs:
        cantidad += 1
    return cantidad


def lista_atributos(**kwargs):
    lista =[]
    for kwargs in kwargs:
        lista.append(kwargs)
    return lista


def describir_persona(nombre, **kwargs):
    print(f"Caracteristicas de {nombre}: ")
    for a, b in kwargs.items():
        print(f"{a}:  {b}")


if __name__ == "__main__":
    print(cantidad_atributos(23, "hola", 54, 32, 98, 99, y=3, t=7, z=5, u=98))
    print(lista_atributos(a=1, b=2, c=3))
    print(describir_persona("daniel", ojos="cafes", pelo="castanio", estatura=174))