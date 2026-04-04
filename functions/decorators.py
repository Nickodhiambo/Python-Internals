#!/usr/bin/env python

def logged(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] {func.__name__} takes {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'[LOG] {func.__name__} returns {result}')
        return result
    return wrapper
