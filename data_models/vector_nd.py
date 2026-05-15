#!/usr/bin/env python

"""
Implements a multidimensional vector that behaves like
Python's native sequence type
"""

import math
import reprlib
from array import array
from typing import Iterable
from functools import reduce
import operator
import itertools

class Vector:
    typecode = 'd'
    def __init__(self, components: Iterable):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('[')\
                :-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return len(self) == len(other) and\
                all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return reduce(operator.xor, hashes, 0)

    def abs(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    # Methods to make vector a sequence
    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        import operator
        index = operator.index(key)
        return self._components[index]

    # Implement operators
    # Unary
    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    # Infix
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(
                self, other, fillvalue=0.0
                )
            return Vector(a+b for a,b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return Vector(n * factor for n in self)

    def __rmul__(self, scalar):
        return self * scalar
