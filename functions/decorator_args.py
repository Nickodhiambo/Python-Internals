#!/usr/bin/env python

"""
A decorator that takes arguments
"""
from functools import wraps

def repeat(n):
    """
    Runs a function n times
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
