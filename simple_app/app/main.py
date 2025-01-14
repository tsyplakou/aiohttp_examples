import os

import aiohttp_jinja2
import jinja2
from aiohttp import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


async def create_app():
    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))
    app.router.add_get('/', index_handler)

    return app


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    return {"title": "Aiohttp Web App", "message": "Привет из Aiohttp!"}


if __name__ == "__main__":
    web.run_app(create_app(), host='127.0.0.1', port=8080)
