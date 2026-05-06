#!/usr/bin/env python

"""
Provides a Car class that subclasses different types of
car
"""

from abc import abstractmethod, ABC

class Car(ABC):
    """
    Defines a car base class
    """
    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def means_of_propulsion(self):
        pass

    @abstractmethod
    def horse_power(self):
        return '0'

    def describe(self):
        make = self.make()
        fuel = self.means_of_propulsion()
        power = self.horse_power()

        return f'A {fuel}-powered {make} with {power} horse power '


class Tesla(Car):
    def make(self):
        return 'Tesla Model Y'

    def means_of_propulsion(self):
        return 'electric'

    def horse_power(self):
        return '100'


class IncompleteCar(Car):
    def make(self):
        return 'Toyota'

    def means_of_propulsion(self):
        return 'petrol'


class BasicCar(Car):
    def make(self): return 'Sedan'
    def means_of_propulsion(self): return 'diesel'
    def horse_power(self):
        base = super().horse_power()
        return f'{base}'
