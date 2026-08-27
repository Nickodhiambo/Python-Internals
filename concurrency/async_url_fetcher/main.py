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
    async with session.get(url) as response:
        if response:
            try:
                data = await response.json()
                return data
            except:
                print('Error: Failed to parse JSON')
        else:
            print('Error: Failed to fetch')

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
