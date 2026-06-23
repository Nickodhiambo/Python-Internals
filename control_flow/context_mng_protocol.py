#!/usr/bin/env python

"""
Implemnts a custom context manager protocol for file
opening, similar to 'with' statement
"""

class CustomContext:
    """
    A context manager object that mimics the with statement.
    The manager defines 'enter' and 'exit' magic methods
    required to implement the context manager protocol.
    enter runs when with is invoked and it binds the object it returns to the variable defined in the with invocation.
    exit receives exception raised within the with block or
    None if there is no exception raised. If exit is
    implemented such that it returns False, it means the
    programmer has opted to persist/propagate the exception returned,else, the exception is purposely supressed
    """
    def __init__(self, path: str, mode: str):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print('Opening file...')
        self.file = open(self.path, self.mode)
        # Binds to the variable provided in with...as f'
        return self.file

    def __exit__(self, exec_type, exec_val, exec_tb):
        print('Closing file...')
        self.file.close()
        return False # Do not supress exception
