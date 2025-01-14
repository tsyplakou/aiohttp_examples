from aiohttp import web
import asyncio
import asyncpg
import json


def dumps(data):
    if isinstance(data, asyncpg.Record):
        return json.dumps(dict(data))
    elif isinstance(data, list):
        return json.dumps([dumps(item) for item in data])
    return json.dumps(data)


async def create_connection():
    conn = await asyncpg.connect(
        user='postgres',
        password='postgres',
        database='library_26',
        host='localhost',
    )
    return conn


async def read_user(user_id):
    conn = await create_connection()
    value = await conn.fetchrow(
        'SELECT id, username FROM user_user WHERE id = $1',
        user_id,
    )
    await conn.close()

    return value


async def read_users():
    conn = await create_connection()
    records = await conn.fetch('SELECT id, username FROM user_user')
    await conn.close()

    return list(dict(record) for record in records)


async def get_users(request):
    return web.json_response(await read_users(), dumps=dumps)


async def get_user(request):
    user_id = int(request.match_info['id'])
    user = await read_user(user_id)
    if user:
        return web.json_response(user, dumps=dumps)
    return web.json_response({"error": "User not found"}, status=404)


async def create_app():
    app = web.Application()
    app.router.add_get('/users', get_users)
    app.router.add_get('/users/{id}', get_user)
    return app


if __name__ == "__main__":
    web.run_app(create_app())
