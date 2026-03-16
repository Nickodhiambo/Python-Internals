#!/usr/bin/env python

def operators():
    """
    Demonstrates how set operators Like Union (|) and 
    Intersection (&) reduces amount of code

    Assume have a smaller (needle) and larger(haystack)
    number of email addresses. You want to count how
    many needles occur in haystack
    """

    # Naive way
    found = 0
    for n in needles:
        for n in haystack:
            found += 1

    # Optimal way
    found = len(needles & haystack)
