#!/usr/bin/env python

"""
Creating a user defined callable:
    A callable in python is any object that implements
    the dunder method __call__
    Functions, classes and methods are callable by default
    A callable is invoked using parenthesis () after its
    constructor
"""
import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from an empty\
                    BingoCage')

    def __call__(self):
        return self.pick()
