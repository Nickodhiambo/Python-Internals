#!/usr/bin/env python
"""
This module investigates the working of the dynamic
attribute tool `property`. When the property decorator is set on an attribute it allows the programmer to add
more logic to attribute access without changing the
attribute's interface.
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Balance cannot be less than 0')

    @balance.deleter
    def balance(self):
        raise AttributeError('Cannot delete balance')

acc = BankAccount(5000)
print(acc.balance) 
#Access interface is the same as if it were a normal attribute
acc.balance = 10000
acc.balance = -500 # Would raise value error
del acc.balance # Would raise attribute error
