from aiohttp import web

routes = web.RouteTableDef()


# flask style
@routes.get('/')
@routes.post('/')
async def handler(request):
    return web.Response(text="Hello, world!")

if __name__ == '__main__':
    app = web.Application()
    # app.add_routes(routes)
    # or django style
    app.router.add_routes([
        web.get('/', handler),
        web.post('/', handler),
        web.get('/milk/', handler),
        web.post('/milk/', handler),
    ])
    web.run_app(app)
