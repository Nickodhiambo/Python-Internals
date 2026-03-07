#!/usr/bin/env python

def cartesian_products():
    """Use list comp to generate a cartesian product of
    nested loops
    """
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    tshirts = [(color, size) for color in colors
               for size in sizes]
    return tshirts
