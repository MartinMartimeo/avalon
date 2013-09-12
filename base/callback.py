#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Callbacks for successfull model changes
"""
from urllib.parse import urljoin
from base.handler import RequestHandler
from tornado_restless.wrapper import ModelWrapper

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '12.09.13 - 15:55'


def after_redirect(result: dict, model: ModelWrapper, handler: RequestHandler, *, url: str):
    """
        Redirects to a given url after a model successfull changed/added/removed

        :param result: The return result (for get_single and post this is the instance as dict)
        :param model: Modified model
        :param handler: Request Handler
        :param url: The given url to redirect
    """

    primary_key = len(model.primary_keys) > 1 and tuple(model.primary_keys) or list(model.primary_keys)[0]
    handler.redirect(url=urljoin(url, "%s/%s" % (model.__collectionname__, result[primary_key])))
