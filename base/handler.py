#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 22:39'

from alembic.util import memoized_property

from tornado_menumaker import page, index, subpage
from tornado.web import RequestHandler


@page('/', 'The Resistance: Avalon')
class RequestHandler(RequestHandler):
    """
        Base Class
    """

    def initialize(self, **kwargs):
        pass

    @property
    def is_ajax(self):
        """
            Is this an ajax query?
        """
        return self.request.headers.get('X-Requested-With') == "XMLHttpRequest"

    def get_template_namespace(self):
        """
            Inject tempalte namesapce vara
        """
        namespace = super().get_template_namespace()
        namespace["is_ajax"] = self.is_ajax
        return namespace

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
        left = ""
        right = ""
        self.render('app.tpl', left=left, right=right)

    @subpage('/(\w{4,})')
    def page(self, page):
        """
            Page
        """
        left = self.render_string('%s.tpl' % page)
        right = ""
        return self.render('app.tpl', left=left, right=right)

    @subpage('/(\w{4,})/(\w+)')
    def subpage(self, page, sub):
        """
            Sub Page
        """
        left = self.render_string('%s.tpl' % page)
        right = self.render_string('%s-%s.tpl' % (page, sub))
        return self.render('app.tpl', left=left, right=right)