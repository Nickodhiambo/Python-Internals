#!/usr/bin/env python

"""
Creating and managing threads and processes  manually 
is cumbersome. Python provides a high level API,
concurrent.futures, for creating and managing threads
and processes. The API provides executor objects for either
threads or processes. The executor, when invoked, creates
and manages a group of workers, threads or processes, and
assigns tasks to them. The code submits a task to the
executor which delegates to the workers
"""

from concurrent.futures import ThreadPoolExecutor
import requests

# A task defined in a function
def fetch(url: str) -> dict | None:
    response = requests.get(url)
    return response.json()

# Automatically create and manage worker threads using
# futures API
def main():
    urls = [
            "https://jsonplaceholder.typicode.com/users/1",
            "https://jsonplaceholder.typicode.com/users/2",
            "https://jsonplaceholder.typicode.com/users/3"]

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch, urls))
    for item in results:
        print(item['name'])

main()

