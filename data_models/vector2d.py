#!/usr/bin/env python

"""
A simplistic class representing special methods use cases

Addition:
    >>> v1 = (2,4)
    >>> v2 = (2,1)
    >>> v1 + v2
    >>> Vector(4,5)

Absolute value:
    >>> v = Vector(3,4)
    >>> abs(v)
    >>> 5.0

Scalar multiplication:
    >>> v * 3
    >>> Vector(9,12)
    >>> abs(v)
    >>> 15.0
"""
import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar

        return Vector(x, y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))
