"""
TDD using pytest
test file for BankAccount class
"""
# Below import statement implies - BankAccount class is being imported from file Bank_Account
from Bank_Account import BankAccount

# function to test the deposit() func of BankAccount
# create a BankAccount Object
# Call the deposit() func
# assert check the balance if it contains correct balance after deposit()
def test_deposit():
    account = BankAccount(124124,100)
    assert account.getAcctNum() == 124124
    account.deposit(270)
    assert account.getBalance() == 360

# function to test the withdraw() func of BankAccount
# create a BankAccount Object
# Call the withdraw() func
# assert that balance is correct after withdraw()
def test_withdraw():
    account = BankAccount(2345667, 200)
    assert account.getAcctNum() == 2345667
    account.withdraw(50)
    assert account.getBalance() == 150