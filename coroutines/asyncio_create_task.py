#!/usr/bin/env python
"""
Use 'asyncio.create_task' to schedule tasks independently
and then await their return. This gives you a finer
control over running coroutines concurrently. You could
schrdule coroutines to run, do other things then await
their return later
"""
import asyncio

async def task(name: str, delay: int) -> str: 
    print(f'task {name} started')
    await asyncio.sleep(delay)
    print(f'task {name} finished')
    return name

async def main():
    # Schedule tasks independently
    task_a = asyncio.create_task(task('A', 2))
    task_b = asyncio.create_task(task('B', 1))
    task_c = asyncio.create_task(task('C', 3))

    # Do other stuff
    # ...

    # tasks are already running, now we await their results
    result_a = await task_a
    result_b = await task_b
    result_c = await task_c

    print(f'results: {result_a}, {result_b}, {result_c}')

asyncio.run(main())
