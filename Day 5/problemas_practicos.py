def devolver_distintos():
    pass


def unicas(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista


def ceros_vecinos(*args):
    contador =0




if __name__ == "__main__":
    print(unicas("melocoton"))