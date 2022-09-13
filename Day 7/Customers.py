import Person as p


class Customers(p.Person):
    def __int__(self, nombre, apellido, ncuenta, balance):
        super().__int__(nombre, apellido)
        self.ncuenta = ncuenta
        self.balance = balance
