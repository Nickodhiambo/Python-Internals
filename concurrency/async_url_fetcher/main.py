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
        return None
    except asyncio.TimeoutError:
        print (f'Request to {url} is timed out')
        return None

BASE_URL = 'https://jsonplaceholder.typicode.com'

async def fetch_user_with_posts(
        user_id: int, session: aiohttp.ClientSession)-> dict | None:
    """Fetches a user, uses user id to build post url then fecthes the user's post"""
    user = await fetch(
            f'{BASE_URL}/users/{user_id}', session)

    #No need to fetch posts if user is None
    if user is None:
        return None
    
    # Now fetch posts
    posts = await fetch(
            f'{BASE_URL}/posts?userId={user["id"]}', session)

    if not posts:
        return None

    # Return a dict combining user with posts information
    return {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'post_count': len(posts),
            'posts': [p['title'] for p in posts]
            }

async def main():
    user_ids = [1,2,3]
    # Set a timeout so requests don't hang indefinitely
    to = aiohttp.ClientTimeout(total=10) # maximum 10 seconds
    # Fetch several urls concurrently
    async with aiohttp.ClientSession(timeout=to) as session:
        # Coroutine object for every request is stored
        # in tasks
        tasks = [fetch_user_with_posts(
            user_id, session) for user_id in user_ids]
        # Event loop automatically schedules and executes
        # all the coroutine objects concurrently
        results = await asyncio.gather(*tasks)
    
    successful = [r for r in results if r is not None]

    for user in successful:
        print(f" {'*' * 40}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Number of posts: {user['post_count']}")
        for post in user['posts']:
            print(post)

asyncio.run(main())
