#!/usr/bin/env python
"""
The async url fetcher makes makes HTTP requests with any
number of urls passed to it concurrently. The fetcher
uses the asyncio concurrency model; which creates a
single thread and multiple coroutines as execution
blocks, managed by the Python's Event Loop.
The fetcher takes advantage of the asyncio library to
provide the event loop, and aiohttp library, an
asynchronous HTTP library, similar in functionality
to `requests` library but with async support
"""

import asyncio
import aiohttp

# Implement a coroutine to act as a generic fetcher
async def fetcher(
        url: str, session: aiohttp.ClientSession)->dict|None:
    """A generic fetcher that takes  url string passed to it
    and retrieves response from a server

    Args:
    url: str: A url string
    session: An HTTP connection session between client
             and server
    Returns: Json response if connection to server is
             successful, else None
    """

    print(f'Fetching {url}')

    # Try establishing a connection with server
    try:
       async with session.get(url) as response:
            # if we get a response...
            if response.status == 200:
                try:
                    data = await response.json()
                    return data
                except aiohttp.ContentTypeError:
                    print('Response is not valid JSON')
                    return None
            else: 
                # Connection was established but we have a
                # HTTP (status 4XX and 5XX)
                print(f'Error: HTTP {response.status} for {url}')
                return None
    # If connection is not successful, handle network
    # level errors
    except aiohttp.ClientConnectionError:
        # Client/server is offline,
        # url is incorrect or broken
        # server is unavailable
        print('Connection error: {url} failed to connect')
        return None
    except asyncio.TimeoutError:
        # Slow network
        print(f'Connection Error: {url} is taking too long')
        return None

    except aiohttp.InvalidUrlClientError:
        # Handle invalid URL
        print(f'Invalid url for {url}')
        return None

BASE_URL = 'https://jsonplaceholder.typicode.com'

# A coroutine to fetch a user's posts
async def fetch_user_with_posts(
        userId: int, session: aiohttp.ClientSession
        ) -> dict | None:
    # Get a user
    user = await fetcher(
            f'{BASE_URL}/users/{userId}', session)
    # No need to fetch posts if user is None
    if not user:
        return None
    # Fetch posts for that user if they exist
    posts = await fetcher(
            f"{BASE_URL}/posts?userId={user['id']}", session)
    # Return a combined user and post data
    return {'name': user['name'],
            'email': user['email'],
            'posts': posts
            }

async def main():
    user_ids = [1,2,3]

    # Set a timeout so connections do not hang indefinitely
    to = aiohttp.ClientTimeout(total=10) # 10s

    # Create a HTTP session for fetcher and start event loop
    async with aiohttp.ClientSession() as session:
        # Calling fetcher returns coroutine objects
        coro_tasks = [
                fetch_user_with_posts(
                    user_id, session) for user_id in user_ids
                ]
        # Run the coroutines concurrently with event loop
        results = await asyncio.gather(*coro_tasks)

    # Filter out unsuccessful tasks
    successful = [r for r in results if r is not None]
    for r in successful:
        print(f"{'*' * 50}")
        print(f"Name: {r['name']}")
        print(f"Email: {r['email']}")
        for p in r['posts']:
            print(p)
        print(f"{'  ' * 50}")

# Run event loop
asyncio.run(main())
