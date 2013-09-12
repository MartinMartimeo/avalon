#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:00'

from functools import partial

import yaml
from sqlalchemy import create_engine
from sqlalchemy.util.langhelpers import memoized_property
from sqlalchemy.orm import sessionmaker, scoped_session
from tornado.web import Application
from tornado.ioloop import IOLoop

import environment
from tornado_menumaker import routes
from tornado_restless import ApiManager as RestlessManager
from tornado_backbone import ApiManager as BackboneManager

from . import logger
from .callback import after_redirect

from models import metadata, character, room, user


class Application(Application):
    """
        Base Class
    """

    def __init__(self, **settings):

        for key in dir(environment):
            if not key.startswith("_"):
                settings.setdefault(key, getattr(environment, key))

        #noinspection PyUnresolvedReferences
        from base.handler import RequestHandler

        super().__init__(routes(), **settings)

        self.create_api()

    def create_api(self) -> "[ApiManager, ApiManager]":
        """
            Restless & Backbone API
        """
        logger.debug("Create Api Engine")

        restless = RestlessManager(application=self, session_maker=self.database)
        backbone = BackboneManager(application=self)

        models = [character.DbCharacter, room.DbRoom, user.DbUser]

        for model in models:
            restless.create_api(model,
                                methods=RestlessManager.METHODS_ALL,
                                postprocessor=dict(
                                    post=[partial(after_redirect, url="/%s/show" % model.__tablename__)]))
            backbone.create_api(model)

    @staticmethod
    def start():
        """
            Starts the IOLoop
        """
        logger.info('Starting IOLoop instance')
        IOLoop.instance().start()

    @memoized_property
    def database(self) -> sessionmaker:
        """
            constructs the database connection and fills it with data
        """

        logger.info('Starting database connection')
        dns = self.settings['dns']

        if dns.startswith("sqlite"):
            engine = create_engine(dns, connect_args={'isolation_level': None})
        else:
            engine = create_engine(dns)
        engine.connect()

        metadata.bind = engine
        metadata.create_all(engine)

        factory = sessionmaker(bind=engine, autoflush=True)
        scope = scoped_session(factory)
        session = scope()

        for char in yaml.load(open('data/characters.yaml')):
            logger.debug(char)
            char = character.DbCharacter(**char)
            session.merge(char)

        session.commit()
        session.close()

        return scope


