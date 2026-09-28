class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance

    def withdraw(self, amount):
        if(self.__balance < amount):
           print("current balance:",self.__balance)
           raise print("Insufficent funds")

        self.__balance = self.__balance - amount
        return self.__balance
    def get_balance(self):
        return self.__balance

acc = BankAccount(50)
print(acc.deposit(1000))
print(acc.get_balance())
    