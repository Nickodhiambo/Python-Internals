#!/usr/bin/env python

"""
Provides a Sentence class object that implements
the Iterable pattern in Python
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    """
    A class object that behaves like an iterable
    """
    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    # Implement iterable protocol
    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

class SentenceIterator:
    """
    Implements the Iterator Design Pattern
    """
    def __init__(self, words):
        self.words = words
        self.index  = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[index]
        except IndexError:
            StopIteration()
        self.index += 1
        return word
