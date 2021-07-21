# Starts Gevent which runs Flask

from gevent.pywsgi import WSGIServer
from wendy.app import app


def start_gevent(app_port):
    http_server = WSGIServer(('127.0.0.1', app_port), app)
    http_server.serve_forever()


if __name__ == "__main__":
    start_gevent(5000)