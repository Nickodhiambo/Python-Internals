#!/usr/bin/env python
"""
This script downloads and saves flag images of 20 most
populous countries in the world concurrently, and
displays download progress on the terminal.
The asyncio concurrency model is used to achieve concurrent
downloads
"""
import asyncio

from httpx import AsyncClient
from flags import BASE_URL, main, save_flag

async def download_one(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                      follow_redirects=True)
    return resp.read()

def download_many(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))

async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        tasks = [download_one(client, cc) for cc\
                in sorted(cc_list)
                ]
        res = await asyncio.gather(*tasks)
    return len(res)

if __name__ == '__main__':
    main(download_many)
