
import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.bank_account import BankAccount;

class testBankAccount(unittest.TestCase):
 def test_deposit(self):
     #creating an object of class
    s = BankAccount(1000, "Swarna")
    bal = s.balance()
    self.assertEqual(bal, 1000)
    self.assertEqual(s.name(), "Swarna")
    #calling functions with that class
    self.assertEqual(s.deposit(550), 1550)
 def test_withdraw(self):
    #creating an object of class
    s = BankAccount(1500, "Swarna")
    self.assertEqual(s.withdraw(1000), 500)
    self.assertEqual(s.balance(), 500)
    self.assertRaises(Exception, s.withdraw, 600)

if __name__ == "__main__":
     unittest.main(verbosity=2)