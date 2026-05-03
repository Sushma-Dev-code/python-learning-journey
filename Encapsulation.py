class Bank:
    def __init__(self):
        self.__balance=1000 #private variable
    def deposit(self, amount):
        self.__balance+=amount
    def show_balance(self):
        return self.__balance
    
b=Bank()
b.deposit(500)
print(b.show_balance())
print(b.deposit(400))
print(b.show_balance())
