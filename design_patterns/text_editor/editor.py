#!/usr/bin/env python
"""
Provides an interface that exposes a primitive text editor
core functionality:
    insert: Add text
    delete: erase text
"""

class TextEditor:
    def __init__(self):
        """
        Initializes an editor with empty text
        """
        self._content = ''

    def insert(self, text: str):
        """
        inserts a string of text into editor
        """
        self._content += text
        print(f'Content: {self._content}')

    def delete(self, n_chars: int):
        """
        Deletes n_chars number of char from content
        """
        self._content = self._content[:-n_chars]
        print(f'Content: {self._content}')
