import Person as p


class Cliente(p.Person):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Numero de cuenta: {self.numero_cuenta} Balance: {self.balance}"


    def depositar(self, monto):
        self.balance += int(monto)
        print("Deposito realizado. ")


    def retirar(self, monto):
        if monto > self.balance:
            print("No es posible realizar el retiro")
        else:
            self.balance -= int(monto)
            print("Retiro realizado. ")
    

