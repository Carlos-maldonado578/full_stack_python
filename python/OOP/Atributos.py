class User:                 #declare la clase y dele un nombre de usuario
    def __init__(self):
        self.name = 'Michael'
        self.email = 'michael@codingdojo.com'
        self.account_balance = 0

guido = User()
monty = User()

print(guido.name)
print(monty.name)

guido.name = "Guido"
monty.name = "Monty"

print(guido.name)
print(monty.name)

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)
print(monty.name)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount

guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)