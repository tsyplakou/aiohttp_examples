import aiohttp
import asyncio
from aiohttp import BasicAuth

# async def main():
#     async with aiohttp.ClientSession() as session:
#         # Отправляем запрос и получаем куки
#         async with session.get('https://httpbin.org/cookies/set?name=value') as response:
#             print("Cookies set:", response.cookies)
#
#         # Автоматически отправляем куки на следующий запрос
#         async with session.get('https://httpbin.org/cookies') as response:
#             print("Cookies sent:", await response.text())


# async def main():
#     headers = {'User-Agent': 'MyApp/1.0'}
#     async with aiohttp.ClientSession(headers=headers) as session:
#         async with session.get('https://httpbin.org/headers') as response:
#             print(await response.text())


# async def main():
#     auth = BasicAuth('username', 'password')
#     async with aiohttp.ClientSession(auth=auth) as session:
#         async with session.get('https://httpbin.org/basic-auth/username/password') as response:
#             print(await response.text())


async def main():
    timeout = aiohttp.ClientTimeout(total=10)  # 10 секунд на запрос
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.get('https://httpbin.org/delay/5') as response:
                print(await response.text())
        except asyncio.TimeoutError:
            print("Запрос превысил лимит времени")


if __name__ == '__main__':
    asyncio.run(main())
