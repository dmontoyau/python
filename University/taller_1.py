import numpy as np


def punto_1(a):
    pares = 0
    prom_pares = []
    prom_impares = []
    total_pares = 0
    impares = 0
    total_impares = 0
    for i in a:
        if i % 2 == 0:
            pares += i
            prom_pares.append(i)
            total_pares += 1
        else:
            impares += i
            prom_impares.append(i)
            total_impares += 1
    print(f"\nEl total de los pares es: {pares}, y su primedio es: {np.mean(prom_pares)}")
    print(f"El total de los impares es: {impares}, y su primedio es: {np.mean(prom_impares)}")



def punto_3(vector):
    vector.sort()
    print("""
    punto 3: Organizar vector:
    """)
    print(vector)


"""def punto_4(vector, dato):

    while vector != dato:
"""

def main():
    a = np.array([45, 45, 67, 20, 1, 8, 24, 31, 4, 5, 6])
    print(a)
    punto_1(a)
    punto_3(a)


if __name__ == "__main__":
    main()
