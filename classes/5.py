class Account:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if money > self.balance:
            print("Low balance")
        else:
            self.balance -= money
            print("Success")

a = Account("Anita", 0)
a.withdraw(100)
a.deposit(200)
a.withdraw(10)