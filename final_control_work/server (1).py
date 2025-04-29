import io
import logging
from contextlib import contextmanager, redirect_stdout
from json import dumps
from multiprocessing import Process
from time import sleep

from flask import Flask

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {"genie": "Zagan", "event": "rebuff", "year": 1170, "place": "Baghdad"},
        {"genie": "Phenex", "event": "escape", "year": 1759, "place": "Hajar"},
        {"genie": "Phenex", "event": "resistance", "year": 1131, "place": "Baghdad"},
        {"genie": "Lane", "event": "disobedience", "year": 1415, "place": "Sanaa"},
        {"genie": "Phenex", "event": "escape", "year": 1021, "place": "Baghdad"},
        {"genie": "Phenex", "event": "disobedience", "year": 981, "place": "Mecca"},
        {"genie": "Phenex", "event": "response", "year": 1547, "place": "Hajar"},
        {"genie": "Agares", "event": "response", "year": 1058, "place": "Damascus"}
    ]

    server = Server('127.0.0.1', 8080, data)
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
