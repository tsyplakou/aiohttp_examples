# pip install aiohttp
from aiohttp import web


async def handler_get(request):
    param = request.query.get('param', default='World')
    return web.Response(text="Hello, {}!".format(param))


async def handler_post(request):
    param = (
        await request.json()
    ).get('param', 'World')
    return web.Response(text="Hello, {}!".format(param))


app = web.Application()
app.router.add_get('/hello', handler_get,  allow_head=False)
app.router.add_post('/hello', handler_post)


if __name__ == '__main__':
    web.run_app(app)
