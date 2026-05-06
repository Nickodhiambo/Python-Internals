#!/usr/bin/env python
"""
Provides an Animal abstract base class
"""
from abc import abstractmethod, ABC

class Animal(ABC):
    """
    An abstract Animal class that provides the methods all 
    Animal subclasses must have
    """
    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def mode_of_reproduction(self):
        pass

    def describe(self):
        # A concrete method. subclasses do not need to
        # implement this
        move = self.movement()
        reproduce = self.mode_of_reproduction()
        return f'This animal moves by {move} and reproduces by {reproduce}'

class Dog(Animal):
    """
    A Dog subclass inheriting from Animal ABC
    """
    def movement(self):
        return 'walking'

    def mode_of_reproduction(self):
        return 'sexual reproduction'
