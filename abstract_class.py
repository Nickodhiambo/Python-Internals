#!/usr/bin/env python

"""
A custom abstract base class
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        # Isn't meant to be implemented in the abstract
        # base class
        # Will be extended in the subclass. But the subclass
        # Must implement it
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
