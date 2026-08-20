#!/usr/bin/env python
"""
We can automate the creation, running, and closing of
coroutines using the event loop. Event loop is
capable of managing thousands of coroutines
concurrently by cooperative scheduling. At await points,
event loop switches to another coroutine.
Below is a two coroutines that run sequentially. Event
loop does not switch at await points
"""

import asyncio # Python library that creates an event loop
import time

async def task(name, delay):
    print(f'Started {task}')
    # Suspend coroutine here
    await asyncio.sleep(delay)
    print(f'{name} Finished after {delay}s')

async def main():
    await task('A', 2)
    await task('B', 1)

start = time.time()
asyncio.run(main()) # Entry pt to event loop
print(f'Time taken: {time.time() - start:.2f}s')
