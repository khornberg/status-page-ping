import aiohttp
import asyncio
import time
from datetime import datetime
from collections import namedtuple

default_urls = ['http://python.org']


def make_408(url):
    Response = namedtuple('Response', ['status', 'reason', 'url', 'headers'])
    date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    return Response(408, 'Request Timeout', url, {'Date': date})


async def fetch(session, url):
    try:
        async with session.get(url, timeout=3) as response:
            return response
    except asyncio.TimeoutError:
        return make_408(url)


async def ping(loop, url):
    async with aiohttp.ClientSession(loop=loop) as session:
        start = time.time()
        response = await fetch(session, url)
        elasped = time.time() - start
        return {
            'status': response.status,
            'reason': response.reason,
            'url': url,
            'elasped': elasped,
            'dtg': datetime.strptime(response.headers.get('Date'), '%a, %d %b %Y %H:%M:%S GMT').timestamp()
        }


async def get_pings(loop, urls):
    return [await ping(loop, url) for url in urls]


def get(_urls=None):
    urls = _urls or default_urls
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(get_pings(loop, urls))


if __name__ == '__main__':
    print(get())
