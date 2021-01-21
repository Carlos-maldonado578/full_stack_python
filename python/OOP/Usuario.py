class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal (self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Saldo insuficiente")

    def display_user_balance (self):
        return self.name, self.account_balance



guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
roro = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(200)
guido.make_withdrawal(100)
print(guido.display_user_balance())
print()
monty.make_deposit(200)
monty.make_deposit(100)
monty.make_withdrawal(100)
print(monty.display_user_balance())
print()
roro.make_deposit(200)
roro.make_withdrawal(100)
roro.make_withdrawal(50)
print(roro.display_user_balance())