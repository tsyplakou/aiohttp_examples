bind = "unix:/tmp/aiohttp_app.sock"
workers = 1
worker_class = "aiohttp.GunicornWebWorker"
# gunicorn -c gunicorn_config.py app.main:create_app
