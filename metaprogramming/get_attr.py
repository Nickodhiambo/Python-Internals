#!/usr/bin/env python
"""
This module implements the __getattr__ object method ina user-defined class. The method is implemented in the native python object that all user-defined objects inherit from.

If __getattr__ is implemented explicitly in a 
user-defined object, it overrides the native object's
implementation.

Explicit implementation in a user class is usually doneto handle missing attributes gracefully, and to be ableto access attribue data using dot notation,
which is a cleaner way than using brackets, in case the
data is a mapping. 
"""

class User:
    def __init__(self, data: dict):
        self._data = data

    def __getattr__(self, name):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(
                    f'attribute {name} does not exist')


user = User({'name': 'Nick'})
print(user.name)
print(user.age)

