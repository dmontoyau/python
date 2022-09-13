import Cliente as c


def crear_cliente ():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el Apellido del cliente: ")
    ncuenta = int(input("Ingrese el numero de su cuenta: "))
    balance = int(input("Ingrese el numero de su balance: "))
    nuevo = c.Cliente(nombre, apellido, ncuenta, balance) 
    return nuevo


def menu():
    opcion= int(input(""" Que desea ralizar
              [1] Consignar
              [2] Retirar
              [3] Salir
              """))
    return opcion
              

if __name__ == "__main__":
    nuevo = crear_cliente()
    print(nuevo)
    opcion = "x"
    finalizar = False
    
    while opcion != 3:
        opcion = menu()
        if opcion == 1:
            monto = int(input("Cuanto dinero va depositar? "))
            nuevo.depositar(monto)
        elif opcion == 2:
            monto = int(input("Cuanto dinero va a retirar? ? "))
            nuevo.retirar(monto)
            if monto > nuevo.balance:
                print("No es posible realizar el retro ya que no cuenta con suficientes fondos")
            else:
                nuevo.retirar(monto)
        elif opcion == 3:
            finalizar = True
        else:
            print("Opcion no valida")
            
        print(nuevo.__str__())
        
        
        
        
        
        
        
        