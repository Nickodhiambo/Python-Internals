#!/usr/bin/env python

"""
A class-based implementation of an averager functionality
that computes the average of a series of numbers passed to
it. For every new number passed to the object, it
computes the new average
"""

class Averager:
    def __init__(self):
        self.series = [] # Keep a record of previous values

    def __call__(self, new_val): # Make our object callable
        self.series.append(new_val)
        total = sum(self.series)
        return total / len(self.series)


