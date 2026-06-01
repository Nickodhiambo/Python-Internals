#!/usr/bin/env python

from iterator import NumberRange, NumberRangeIterator

if __name__ == '__main__':
    r = NumberRange(1, 3)

    # Each call to iter produces a fresh iterable
    it1 = iter(r)
    it2 = iter(r)

    print(next(it1))
    print(next(it1))
    print(next(it2))
    # next(it1) # raises stop iteration error

    for n in r:
        print(n)
