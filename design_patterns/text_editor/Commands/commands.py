#!/usr/bin/env python

"""
Create commands that wrap around each object:
    commands are callable objects that captures the state
    of the object
"""

from editor import TextEditor

class InsertCommand:
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.insert(self.text)

    def undo(self):
        self.editor.delete(len(self.text))


class DeleteCommand:
    def __init__(self, editor: TextEditor, n_chars: int):
        self.editor = editor
        self.n_chars = n_chars
        self.deleted_text = ''

    def execute(self):
        self.deleted_text = self.editor.content\
                [-self.n_chars:]
        self.editor.delete(self.n_chars)

    def undo(self):
        self.editor.insert(self.deleted_text)
