#!/usr/bin/env python

"""
Implements a multidimensional vector that behaves like
Python's native sequence type
"""

import math
import reprlib
from array import array
from typing import Iterable

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
        return tuple(self) == tuple(other)

    def abs(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    # Methods to make vector w sequence
    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        import operator
        index = operator.index(key)
        return self._components[index]

    def __hash__(self):
        return 1
