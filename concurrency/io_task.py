#!/usr/bin/env python

"""
Concurency excels in input-output tasks in python
because threads wait in parallel. Execution is still one
thread at a time. Threads automatically release GIL during
IO operations allowing other threads to run
"""

import requests
import threading
import time

urls = ['https://www.google.com',
        'https://smis.uonbi.ac.ke',
        'https://github.com',
        'https://www.amazon.com',
        ]

def fetch(url):
    requests.get(url)

# Execute sequentially
# Each IO operation waits for previous to finish
start = time.time()
for url in urls:
    fetch(url)
print(f'Sequential: {time.time() - start:.2f}s')


# Threading: threads wait in parallel
# There is a speed advantage
start = time.time()
threads = [threading.Thread(
        target=fetch, args=(url),) for url in urls]
for t in threads: t.start()
for t in threads: t.join()

print(f'Threaded: {time.time() - start:.2f}s')

