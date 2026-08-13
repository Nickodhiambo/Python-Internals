#!/usr/bin/env python

"""
A generator function uses the keyword `yield` to produce
one value at a time, unlike a list comprehension which
loads all values at a go into memory.

You need to explicitly call a generator function to return
a generator object. Then use the generator object with
the iterator `next` to yield a value at a time

The yield statement inside the generator function is only
triggered when the generator object is invoked, not when
the generator function is invoked.

Data flow is uni-directional with generators. Once the generator is exhausted, no more values are produced. And you cannot
go back. When called with next, the iterator protocol will
hit the `StopIteration` exception when generator is
exhausted.
"""

def count():
    yield 1
    yield 2
    yield 3

# No value is yielded
# Console will notify you of the memory location
# of the generator object created
print(count())

gen = count()
print(next(gen)) # Yield 1
print(next(gen)) # Yield 2
print(next(gen)) # Yield 3
# Generator exhausted.
# Should throw StopIteration exception
print(next(gen))
