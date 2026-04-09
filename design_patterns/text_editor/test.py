#!/usr/bin/env python

from Commands import InsertCommand, DeleteCommand
from editor import TextEditor
from history import CommandHistory

editor = TextEditor()
history = CommandHistory()

def run_tests():
    print(f"{'=' * 50}")
    print('Initial state')
    print(f"{'=' * 50}")
    editor.show()

    print(f"{'=' * 50}")
    print('Typing Hello')
    print(f"{'=' * 50}")
    history.execute(InsertCommand(editor, 'Hello'))
    editor.show()

    print(f"{'=' * 50}")
    print('Typing World')
    print(f"{'=' * 50}")
    history.execute(InsertCommand(editor, ' World'))
    editor.show()

    print(f"{'=' * 50}")
    print('Deleting 5 characters')
    print(f"{'=' * 50}")
    history.execute(DeleteCommand(editor, 5))
    editor.show()

    print('\n-----------Undo Delete-----------')
    history.undo()
    editor.show()

    print("--------------\nUndo insert 'World'---------")
    history.undo()
    editor.show()

    print('-----------Redo insert World---------')
    history.redo()
    editor.show()
