#!/usr/bin/env python

"""
Provides a state that tracks executed and undone commands
"""

class CommandHistory:
    def __init__(self):
        self._history = [] # Stack to track executed commands
        self._undone = [] # Stack to track undone commands )for redo)

    def execute(self, command):
        """
        Adds an executed command to hitory, clears undone
        """
        command.execute()
        self._history.append(command)
        self._undone.clear() # New action clears redo stack

    def undo(self):
        if not self._history:
            print('Nothing to undo')
            return
        command = self._history.pop()
        command.undo()
        self._undone.append(command)

    def redo(self):
        if not self._undone:
            print('Nothing to redo')
            return
        command = self._undone.pop()
        command.execute()
        self._history.append(command)
