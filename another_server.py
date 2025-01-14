from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, Aiohttp!")


async def echo(request):
    data = await request.text()
    json_data = await request.json()
    return web.Response(text=f"Вы отправили: {data}")


app = web.Application()
app.router.add_get('/hello', hello)  # GET
app.router.add_post('/hello', hello)  # GET
app.router.add_put('/hello', hello)  # GET
app.router.add_patch('/hello', hello)  # GET
app.router.add_delete('/hello', hello)  # GET
app.router.add_post('/echo', echo)  # POST

if __name__ == '__main__':
    web.run_app(app)
