#!/usr/bin/env python

"""
Constructs an iterable and iterator to observe the
iteration mechanism. Iteration, the act of accessing an
item at a time from a collection, works by implementing two
mechanisms; an iterator and an iterable.

Python implements the two mechanisms separately. The 
iterable  mechanism holds or avails a colletion's list of items for the iterator mechanism to act on

The iterator mechanism keeps track of the current item in the collection, how to access the next item, and when the collection is exhausted.

The iterable just avails the collection's data.It does not keep track of which item is under processing, or whether the collection is exhausted. The iterator on the other hand
maintains the traversal state.

To implement an iterable in python, pass __iter__ to an
object. To implement an iterator, one must implement both
__iter__ and __next__
"""

class NumberRange:
    """
    A custom iterable that generates numbers within user
    provided range. Mimics built-in range function
    """
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # Produces an iterator
        return NumberRangeIterator(self.start, self.stop)

class NumberRangeIterator:
    """
    An iterator that tracks state of items in an iterable
    """
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
