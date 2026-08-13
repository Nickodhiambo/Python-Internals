#!/usr/bin/env python

"""
Coroutines are more like advanced generators. Whereas
generators only produce values (yield out values) for their
caller to consume, coroutines yield out values and also
can receive values from the caller.

At a yield point in a generator, a value is sent out. In a 
coroutine, a value is sent out, coroutine is suspended as
waits to receive a value from the caller. coroutine then
resumes when value is sent back.

To drive/run a coroutine:
    1. Invoke the coroutine function
    2. Prime the coroutine, that is, advance it to
       the first yield statement using next
    3. Send a value in

If you send a value into the coroutine without priming it,
you get a TypeError
"""

def simple_coro():
    print('Coroutine started')
    received = yield 1 # Send a value out and receive one inat a yield pt. Received value is stored in the variable received
    print(f'Coroutine received: {received}')
