"""
class keyword is used to define a class in Python followed by the class name
This code snippet defines a class BankAccount with Account Number
and Balance as attribute of the class 
"""
class BankAccount:
    balance = 0
    accountNumber = None
    # This is the initializer function that will be called when this class is instantiated
    # __init__ method is a must in a class
    # This method takes accountNumber and balance as arguments 
    # sets the values passed during object creation to the object's attributes accountNumber and balance
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    # Deposit function credits the account with amount value passed
    def deposit(self, amount):
        self.balance += amount
        print("Account balance is ", self.balance)
        
    # withdraw function debits the account with amount value passed
    def withdraw(self, amount):
        self.balance -= amount
        print("Account balance after withdrawal of amount ",
              amount, " is ", self.balance)

    def getBalance(self):
        return(self.balance)
    def getAcctNum(self):
        return(self.accountNumber)

# Instantiating/creating the BankAccount object with the account number and balance values passed
#account = BankAccount(105234, 1000.00)

# Calls and executes deposit() function of account object
#account.deposit(100)

# Calls and executes withdraw() function of account object
#account.withdraw(50)
