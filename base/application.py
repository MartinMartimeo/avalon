#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:00'

import os

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado_menumaker import page, index, subpage, routes

from . import logger


class Application(Application):
    """
        Base Class
    """

    SETTINGS = {
        'template_path': os.path.join(os.path.dirname(__file__), "..", "templates"),
        'static_path': os.path.join(os.path.dirname(__file__), "..", "static"),
    }

    def __init__(self, **settings):

        for item in self.SETTINGS.items():
            settings.setdefault(*item)

        super().__init__(routes(), **settings)

    @staticmethod
    def start():
        """
            Starts the IOLoop
        """
        logger.info('Starting IOLoop instance')
        IOLoop.instance().start()

