import aiohttp
import asyncio
import time

default_urls = ['http://python.org']


async def fetch(session, url):
    with aiohttp.Timeout(10, loop=session.loop):
        async with session.get(url) as response:
            return response


async def ping(loop, url):
    async with aiohttp.ClientSession(loop=loop) as session:
        start = time.time()
        response = await fetch(session, url)
        elasped = time.time() - start
        return {'status': response.status, 'reason': response.reason, 'url': url, 'elasped': elasped}


async def get_pings(loop, urls):
    return [await ping(loop, url) for url in urls]


def get(_urls=None):
    urls = _urls or default_urls
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(get_pings(loop, urls))
