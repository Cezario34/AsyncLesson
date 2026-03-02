import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import async_timed, fetch_status


@async_timed()
async def main():
	async with aiohttp.ClientSession() as session:
		url = 'https://xn--b1aew.xn--p1ai/'
		status = await fetch_status(session, url)
		print(f'Состояние для {url} было равно {status}')


asyncio.run(main())
