#!/usr/bin/env python
"""
A coroutine that runs forever; at every yield point, the
coroutine takes a value in and yields the running total
out
The coroutine will only close when the running program
raises a 'GeneratorExit' Exception, which happens
when 'close()' is invoked on the coroutine
"""

def coroutine():
    print('Coroutine started')
    total = 0
    while True: # Runs indefinitely
        try:
            # Send current total out, receives new value
            value  = yield total
            # Updates  total
            total += value
        except GeneratorExit:
            print(f'Closing: Total: {total}')
