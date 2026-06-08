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

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

