#!/usr/bin/env python

"""
A python script that retieves flag images from an
online repository one by one (sequentially)and saves them
offline. This is a base script against which we check
how much faster concurrent retrieval and saving is
"""
from pathlib import Path
import time
from typing import Callable

import httpx

country_codes = ('CN IN US ID BR PK NG BD RU JP '
                 'MX PH VN ET EG DE IR TR CD FR'
        ).split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str) -> None:
    """saves a flag img to a directory in a file"""
    (DEST_DIR/filename).write_bytes(img)


def get_flag(cc: str) -> bytes:
    """Gets the flag image online and returns a binary
    content representing the img"""
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    response = httpx.get(
            url, timeout=6, follow_redirects=True)
    response.raise_for_status()
    return response.content

def download_many(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        img = get_flag(cc)
        save_flag(img, f'{cc}.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloader: Callable[[list[str]], int]):
    DEST_DIR.mkdir(exist_ok=True)
    start = time.time()
    count = downloader(country_codes)
    duration = time.time() - start
    print(f'\n{count} downloads in {duration:.2f}s')


if __name__ == '__main__':
    main(download_many)
