#!/usr/bin/env python
"""
A concurrent implementation of an API that downloads
flag inages by country code and stores locally.
Instead of a sequntial download, the API fetches flags
online concurrently by running threads. Threads waiting for
network are in flight simultaenously
"""
from concurrent.futures import ThreadPoolExecutor

from flags import get_flag, save_flag, main

def download_one(cc: str):
    img = get_flag(cc)
    save_flag(img, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    with ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))

if __name__ == '__main__':
    main(download_many)
