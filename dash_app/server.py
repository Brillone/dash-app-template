# base
from concurrent.futures import ThreadPoolExecutor
from waitress import serve

# internal
from app import app, data_update


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(data_update)

    serve(app.server, host='0.0.0.0', port=8080, threads=10)