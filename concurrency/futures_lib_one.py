#!/usr/bin/env python

"""
We use the concurrency.futures library to spawn real OS
processes using ProcessPoolExecutor API. We are doing a
CPU bound task involving heavy computation. Threading
would be inefficient in this case because GIL blocks
threads. A workaround would be to spawn multiple
processes each with its own copy of interpreter and GIL to
achieve concurrency and hence speed up the computation
"""
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_task(n: int) -> int:
    return sum(x**2 for x in range(n))

def main():
    numbers = [1_000_000, 2_000,000, 3_000_000]

    # Try threading; GIL blocks would be slow
    start = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(cpu_task, numbers))
    print(results)
    print(f'TT for threading: {time.time() - start:.2f}s')

    # Multiprocessing is the optimal alternative
    # True parallelism is achieved
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_task, numbers))
    print(results)
    print(f'TT by processes: {time.time() - start:.2f}s')

main()
