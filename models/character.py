#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 21:40'

from . import Base
from .types.id import IdString
from .types.i18n import i18nString
from .types.boolean import Boolean
from .types.integer import Integer


class DbCharacter(Base):
    """
        A character of the game
    """

    __tablename__ = "character"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    _id = IdString("character_id")

    name = i18nString('name')
    name.doc = "Name of the Character"

    is_evil = Boolean()
    is_evil.doc = "Wins with the Minion of Mordred"

    may_fail = Boolean()
    may_fail.doc = "May the character put a fail into a mission"

    may_success = Boolean()
    may_success.doc = "May the character put a success into a mission"

    min_count = Integer()
    min_count.doc = "Is there a minimum count of this character required"