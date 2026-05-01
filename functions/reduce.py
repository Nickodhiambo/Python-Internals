#!/usr/bin/env python
from functools import reduce

def factorial(n: int) -> int:
    return reduce(lambda a, b: a * b, range(1, n+1))
