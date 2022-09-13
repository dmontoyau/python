def run():
    num1 = input("Ingresa un número:")
    num2 = input("Ingresa otro número:")

    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num2 < num1:
        print(f"{num2} es mayor que {num1}")
    elif num2 == num1:
        print(f"{num2} es igual que {num1}")
    else:
        print("no seas mamon")


if __name__=="__main__":
    run()
