#!/usr/bin/env python
"""
Makes use of the the power of closures in python to
implement an efficient version of averager functionality
"""

def make_averager():
    # The inner function will close over these
    # Variables. i.e it will store the values bound to
    # them long after the outer function has returned
    total = 0
    count = 0

    def averager(new_val):
        nonlocal total, count
        total += new_val
        count += 1

        return total / count
    return averager
