#!/usr/bin/env python3
# coding: utf-8

import tornado.ioloop
import tornado.web
import logging
import os
import signal
import sys
import time
import psutil
from tornado.options import define, options, parse_command_line
from tornado.options import options
import config


class MainHandler(tornado.web.RequestHandler):
    def get(self, path=''):
        self.render(path + 'web/index.html', user="")


log = logging.getLogger(__name__)
pid = psutil.Process(os.getpid())

def sig_handler(sig, frame):
    """Catch signal and init callback.
    More information about signal processing for graceful stoping
    Tornado server you can find here:
    http://codemehanika.org/blog/2011-10-28-graceful-stop-tornado.html
    """
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    """Stop server and add callback to stop i/o loop"""
    io_loop = tornado.ioloop.IOLoop.instance()

    logging.info('Will shutdown in 2 seconds ...')
    io_loop.add_timeout(time.time() + 2, io_loop.stop)

def stop_handler(*args, **kwargs):
    sig_handler(*args, **kwargs)



ROOTPATH = os.path.dirname(os.path.abspath(__file__))
I18N_PATH = os.path.join(ROOTPATH, 'i18n')
APPNAME = "eyes"


settings = {
    # Desactiver les deux premieres options pour ameliorer les performances
    "compress_response": True,
    "cookie_secret": "HTo/GueKuoAwBv7cZuKZFezH8FsDKEdTfzVKePokauk=",
    "debug": True,
    "template_path": ROOTPATH,
    "static_path": ROOTPATH,
    "login_url": "/"+APPNAME+"/login",
}

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    router = [
        (r"/", MainHandler),
    ]

    this_app = tornado.web.Application(router, **settings)

    signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGQUIT, stop_handler)
    signal.signal(signal.SIGTERM, stop_handler)

    this_app.listen(8888, options.listen_address)

    current = tornado.ioloop.IOLoop.current()
    current.start()
