#!/usr/bin/env python
import time

def logged(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] {func.__name__} takes {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'[LOG] {func.__name__} returns {result}')
        return result
    return wrapper


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'[TIMED] {func.__name__} ran in {end-start:.4f}s')
        return result
    return wrapper

def validated(func):
    def wrapper(name, *args, **kwargs):
        if not isinstance(name, str) and not name.strip():
            # Name should be a non empty string
            raise ValueError('Variable name must be a non-empty string')
        result = func(name, *args, **kwargs)
        return result
    return wrapper

