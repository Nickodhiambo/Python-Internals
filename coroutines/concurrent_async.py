#!/usr/bin/env python
"""
We could run coroutines concurrently using Python's event loop like this:
"""
import asyncio
import time

async def task(name, delay):
    print(f'Started {name}')
    # Coroutine suspended, event loop switches to another
    await asyncio.sleep(delay)
    print(f'Finished task {name} in {delay}s')
    return f'{name} result'

async def main():
    # Run concurrently
    results = await asyncio.gather(
            task('A', 2),
            task('B', 1),
            task('C', 3),
            )
    print(results)
start = time.time()
asyncio.run(main())
print(f'time taken: {time.time() - start:.2f}s')
