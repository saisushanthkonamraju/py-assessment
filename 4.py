class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance



acct = BankAccount()

acct.deposit(1000)

acct.withdraw(500)

acct.withdraw(800)


print("Balance:", acct.get_balance())

print(acct.__balance)