# coding: utf-8

import os
import sys
import traceback
from tornado.options import define, options, parse_command_line

import logging

logging.basicConfig(format='[%(levelname)1.1s %(asctime)s.%(msecs)03d %(module)s:%(lineno)d] %(message)s',
                datefmt='%F %T')


ROOTPATH = os.path.dirname(os.path.abspath(__file__))

define("https_port", default=8043, help="run on the given secure port", type=int)
define("http_port", default=8080, help="run on the given port", type=int)

define("listen_address", default='0.0.0.0', help="listen address", type=str)

# Working dir
define("appli_dir", default='/home/root/Appli', help="log dir", type=str)
define("assets_dir", default="/home/root/assets", help="Assets directory for shared static ressources (images, stylesheets, ...)", type=str)

define("app", default="pos", help="application type", type=str)

parse_command_line()

