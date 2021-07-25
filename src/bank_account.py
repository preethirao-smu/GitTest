class BankAccount:
    __balance=0
    __name=None
    def __init__(self, bal, nm):
        self.__balance=bal
        self.__name=nm 
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        if self.__balance>=amount:
            self.__balance-=amount
            return self.__balance
        else: raise Exception ("Insufficient balance")
        
    def balance(self):
        return(self.__balance)
    def name(self):
        return (self.__name)