#!/usr/bin/env python

"""
A program that tests the performance of computational
python tasks. Do we have any speed advantage when
computational python tasks execute concurrently over
when they execute sequentially?
"""
import threading
import time

#  Create a computational/cpu bound python task
def cpu_task():
    sum(x ** 2 for x in range(1_000_000))

# Execute sequentially
start = time.time() 
cpu_task()
cpu_task()

print(f'Sequential: {time.time() - start}s') # runs in 0.69s

# Run two threads concurrently
start = time.time()
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)
t1.start(); t2.start()
t1.join(); t2.join()

print(f'Threaded: {time.time() - start}s') # runs in 1.27s

# Conclusion:
# We expect concurrency for computational tasks in python
# to take much less time but it takes even more time, due
# to the overhead of threads competing for the GIL
# The GIL hurts when computational python tasks need to
# execute concurrently
