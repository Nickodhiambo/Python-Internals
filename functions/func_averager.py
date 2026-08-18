#!/usr/bin/env python
"""
A functional-based implementation of averager
functionality
"""

def make_averager():
    series = []

    def averager(new_val):
        series.append(new_val)
        total = sum(series)
        return total / len(series)
    return averager
