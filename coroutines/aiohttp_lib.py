#!/usr/bin/env python
"""
This module demonstrates a real world example of using
asyncio library, in this case using asyncio HTTP library,
aiohttp, to fetch public URLs online concurrently. 
Fecthing concurrently guarantees a linear speed-up. If
you are fecthing 10 URLs it takes 10 times less time.
"""

import asyncio
import aiohttp

# Function that asynchronously fecthes URLs
async def fetch(session, url):
    print(f'Fetching {url}')
    async with session.get(url) as response:
        if response:
            try:
                data = await response.json()
                print(f'Got response from {url}')
                return data
            except:
                print(f'Json format error')
                return {'title': 'No title'}

async def main():
    urls = [
            'https://www.google.com/',
            'https://github.com/',
            ]

    async with aiohttp.ClientSession() as session:
        tasks = [
                fetch(session, url) for url in urls
                ]
        results = await asyncio.gather(*tasks)
    for r in results:
        print(r['title'])

asyncio.run(main())
