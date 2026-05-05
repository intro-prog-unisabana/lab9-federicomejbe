# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return -1
        self.balance -= amount
        return 0

    def __str__(self):
        last_digits = str(self.account_number)[-2:]
        return f"Account Number: **{last_digits}\nCurrent Balance: {self.balance:.2f}"