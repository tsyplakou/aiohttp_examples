import aiohttp
import asyncio


async def fetch(url):
    session = aiohttp.ClientSession()
    try:
        response = await session.get(url)
        data = await response.text()
        print(data)
    finally:
        await session.close()


async def fetch(url):
    async with aiohttp.request('GET', url) as response:
        data = await response.text()
        print(data)


async def fetch():
    async with aiohttp.ClientSession() as session:

        async with session.get(
            'http://localhost:8080/hello',
            params=dict(param='students'),
        ) as response:
            print("Статус:", response.status)
            print("Ответ:", await response.text())

        async with session.post(
            'http://localhost:8080/hello',
            json=dict(param='Python'),
        ) as response:
            print("Статус:", response.status)
            print("Ответ:", await response.text())


if __name__ == "__main__":
    asyncio.run(fetch())
