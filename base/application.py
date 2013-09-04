#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:00'

import environment
import os
import yaml

from alembic.util import memoized_property

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, object_session

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado_menumaker import page, index, subpage, routes

from tornado_restless import ApiManager as RestlessManager
from tornado_backbone import ApiManager as BackboneManager

from . import logger


class Application(Application):
    """
        Base Class
    """

    def __init__(self, **settings):

        for key in dir(environment):
            if not key.startswith("_"):
                settings.setdefault(key, getattr(environment, key))

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

        from models import character, room

        models = [character.DbCharacter, room.DbRoom]

        for model in models:
            restless.create_api(model, methods=RestlessManager.METHODS_ALL)
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

        from models import metadata, character, room

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


