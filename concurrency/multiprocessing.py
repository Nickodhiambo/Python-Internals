#!/usr/bin/env python

"""
To solve speed problem for computational python
scripts, we can use multiprocessing model. In this model,
our code spawns multiple processes, each with its own
Interprater and GIL, running in parallel to each other.
Multiprocessing is usually at a cost of higher memory usage
since each process runs in its own memory space, and
overhead in the inter-process communication.
"""

from multiprocessing import Process
import time

def cpu_task() -> list[int]:
    return [x**2 for x in range(10_000_000)]

start = time.time()
cpu_task()
cpu_task()

print(f'Sequentially: {time.time() - start:.2f}s')

# Create two processes which will run in parallel
p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)

start = time.time()
p1.start(); p2.start()
p1.join(); p2.join()
print(f'Parallel: {time.time() - start:.2f}s')

# Conclusion
# The sequential version runs in about 6s
# The multiprocess model runs in about 3s
# There is a speed advantage in multiprocessing
