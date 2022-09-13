from random import *


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1,dado2

d1,d2=lanzar_dados()
print(f"""
    TUS RESULTADOS DE LOS DADOS FUERON:

        {d1}    {d2}""")

def evaluar_jugada(dado1,dado2):
    print(f"LA JUGADA FUE DE: {dado1 + dado2}")

if __name__ == "__main__":
    evaluar_jugada(d1,d2)