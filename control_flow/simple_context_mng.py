#!/usr/bin/env python

"""
A context manager built using Python built-in contextmanagerdecorator object
"""

from contextlib import contextmanager

@contextmanager
def custom_manager(file: str, mode: str):
    print("opening file...")
    f = open(file, mode)
    
    try:
        yield f # Everything before yield is __enter__

    finally:
        print("Closing file")
        f.close() # Everything after yield is __exit__


