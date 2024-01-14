import asyncio
import aiohttp
from aiohttp import ClientSession
from ch4_concurrent_web_requests import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)

asyncio.run(main())
