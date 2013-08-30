#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 22:39'

from alembic.util import memoized_property

from tornado_menumaker import page, index
from tornado.web import RequestHandler


@page('/', 'The Resistance: Avalon')
class RequestHandler(RequestHandler):
    """
        Base Class
    """

    def initialize(self, **kwargs):
        pass

    @memoized_property
    def db(self):
        """
            Database Session
        """
        return self.application.database()

    @index
    def get(self):
        """
            Index Page
        """

        self.render('app.tpl')
