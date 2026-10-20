#!/usr/bin/env python
"""The set attribute method inherited from `object`
class into a user-degined class implicitly is called
every time an attribute is set in __init__. A user-
defined class can call the method explicitly for
data validation"""

class TypedPoint:
    """All user-defined classes inherit from object"""
    def __setattr__(self, name, value): # Explicitly define __setattr__ for data validation
        if name in ('x', 'y') and not\
                isinstance(value, (int, float)):
                    raise TypeError(
                            f'{name} must be a number, got {type(value).__name__}')
        super().__setattr__(name, value) #Always delegate to super. i.e the setattr method in the superclass

    def __init__(self, x, y):
        self.x = x # Goes through user-defined setattr which will call setattr on superclass
        self.y = y # Goes through setattr

if __name__ == '__main__':
    p = TypedPoint(1,2) # set x = 1, y = 2
    p.x = 'Hello' # Trying to set x dynamically like this would throw an error if x is not a numerical value
