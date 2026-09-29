#!/usr/bin/env python
"""
A concurrent implementation of an API that downloads
flag inages by country code and stores locally.
Instead of a sequntial download, the API fetches flags
online concurrently by running threads. Threads waiting for
network are in flight simultaenously
"""
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future, as_completed

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

def download_many_futures(cc_list: list[str]) -> int:
    """
    Functionality same as download_many. However, instead
    of returning the result of a future object as with
    executor.map(), we return the future object first for
    inspection
    """
    cc_list = cc_list[:5]
    with ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[Future] = []
        # First loop to create and schedule futures
        for cc in sorted(cc_list):
            # .submit method of executor creates a future
            # object
            future = executor.submit(
                    download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        # Second loop to collect results
        for count, future in enumerate(
                as_completed(to_do), 1):
            # Collect result for each future object
            res: str = future.result()
            print(f'{future} result: {res}')
    return count
if __name__ == '__main__':
    main(download_many_futures)
