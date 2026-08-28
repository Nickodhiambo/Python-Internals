#!/usr/bin/env python
"""
An API fetcher to practice on the asyncio concurrency model
in Python. The fetcher sends HTTP requests and parses the
JSON data returned concurrently. All network requests are
in flight at the same time
We use the asyncio and aiohttp libraries to achieve this
"""
import asyncio
import aiohttp

# A coroutine function to fetch data via HTTP request
async def fetch(url: str, session) -> dict:
    print(f'Fetching {url}')
    # We wrap the http request session inside a
    # context manager to automate set up and tear down
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f'Error: HTTP {response.status} for {url}')
                return None
            try:
                data = await response.json()
                return data
            except aiohttp.ContentTypeError:
                print(f'response from {url} is not valid JSON')
                return None
    # Handle network level errors
    except aiohttp.ClientConnectionError:
        print(f'Could not connect to {url}')
        None
    except asyncio.TimeoutError:
        print (f'Request to {url} is timed out')
        None

async def main():
    urls = ['https://jsonplaceholder.typicode.com/users/1',
            # Will raise Json parse
            'https://www.google.com',
            ]
    # Fetch several urls concurrently
    async with aiohttp.ClientSession() as session:
        # Coroutine object for every request is stored
        # in tasks
        tasks = [fetch(url, session) for url in urls]
        # Event loop automatically schedules and executes
        # all the coroutine objects concurrently
        results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
