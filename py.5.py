# Complex Python Program: Mini Bank System

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def show_balance(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")


# Create Account
user = BankAccount("Vikitha", 5000)

# Operations
user.show_balance()
user.deposit(2000)
user.withdraw(1500)
user.withdraw(7000)
user.show_balance()