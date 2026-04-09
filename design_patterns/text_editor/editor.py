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
        self.content = ''

    def insert(self, text: str):
        """
        inserts a string of text into editor
        """
        self.content += text

    def delete(self, n_chars: int):
        """
        Deletes n_chars number of char from content
        """
        self.content = self.content[:-n_chars]

    def show(self):
        """
        Displays the result of an action
        """
        print(f'Content: {self.content}')
