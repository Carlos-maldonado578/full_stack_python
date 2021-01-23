class Cuenta_banco:
    def __init__(self, num, inte, count=0):
        self.numero_cuenta = num
        self.cuenta = count
        self.interes = inte

    def deposito(self, monto):
        self.cuenta += monto
        return self

    def giro(self, monto):
        if self.cuenta >= monto:
            self.cuenta -= monto
        else:
            self.cuenta -= 5
            print("No Money Broh: Se cobra tarifa de $5 :(")
        return self

    def interes_bancario(self):
        if self.cuenta > 0:
            self.cuenta += self.cuenta * self.interes
        return self

    def saldo(self):
        print(self.cuenta); return self

class Usuario:#objetos se escirben con mayuscula y las variables se escriben con minusculas.
    def __init__(self, name, email, num):
        self.name = name
        self.mail = email
        self.cuenta_banco = Cuenta_banco(inte=0.02, count=0, num=num)

    def make_deposito(self, monto):
        self.cuenta_banco.cuenta += monto
        print(self.cuenta_banco.cuenta)
        return self
    def make_withdrawal(self, monto):
        if self.cuenta_banco.cuenta >= monto:
            self.cuenta_banco.cuenta -= monto
        else:
            print("Saldo insuficiente")
        return self
    def display_balance(self):
        print(self.name, self.cuenta_banco.cuenta)
        return self

guido = Usuario("Guido Guidon", "guido@python.cl", 74374673)

guido.make_deposito(100)


