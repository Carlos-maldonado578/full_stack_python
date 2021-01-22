class Cuenta_banco:
	def __init__(self, num, inte):
		self.numero_cuenta = num
		self.cuenta = 0
		self.interes = inte

	def hacer_deposito(self, monto):
		self.cuenta += monto
		return self

	def hacer_retiro(self, monto):
		if self.cuenta >= monto:
			self.cuenta -= monto
		else:
			self.cuenta -= 5
			print("Fondos insuficientes: cobrar una tarifa de $ 5")
		return self

	def interes_bancario(self):
		if self.cuenta > 0:
			self.cuenta += self.cuenta * self.interes
		return self


	def mostrar_saldo(self):
		print(self.cuenta); return self


BCI = Cuenta_banco(555787, 0.01)
Santander = Cuenta_banco(99999, 0.01)

BCI.hacer_deposito(200).hacer_deposito(100).hacer_deposito(50).hacer_retiro(300).interes_bancario().mostrar_saldo()
Santander.hacer_deposito(200).hacer_retiro(100).hacer_retiro(100).hacer_retiro(50).interes_bancario().mostrar_saldo()

