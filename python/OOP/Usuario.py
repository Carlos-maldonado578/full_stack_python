class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal (self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Saldo insuficiente")
        return self
    def display_user_balance (self):
        print(self.name, self.account_balance)
        return self
        #return self



#Instancia de Objeto
guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
roro = User("Rodrigo Salas", "salas@python.com")

# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(200)
# guido.make_withdrawal(100)
# print(guido.display_user_balance())

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
print()
monty.make_deposit(200).make_deposit(100).make_withdrawal(100).display_user_balance()
print()
roro.make_deposit(200).make_withdrawal(100).make_withdrawal(50).display_user_balance()