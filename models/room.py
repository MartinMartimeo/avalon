#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from sqlalchemy.ext.hybrid import hybrid_property

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:41'

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

from . import Base
from .character import DbCharacter
from .types.boolean import Boolean
from .types.id import Id
from .types.integer import Integer
from .types.string import String
from .types.date import DateTime


class DbRoom(Base):
    """
        Represents a room where people can join for a game
    """

    __tablename__ = "room"

    def __init__(self):
        pass

    _id = Id("room_id")

    name = String(maxlen=80, unique=True)
    name.doc = "Name of the Room for display"

    _in_game = Boolean(default=False, info=dict(hidden=True))
    _in_game.doc = "Has the game started?"

    characters = relationship("DbRoom2Character", collection_class=attribute_mapped_collection('_character_id'))
    characters.doc = "Character of Room"

    @hybrid_property
    def in_game(self):
        """
            Game started?
        """
        return self._in_game

    @in_game.setter
    def in_game(self, value):
        """
            Do a sanity check
        """

        # Check Value
        if not value:
            raise AssertionError("Once a game started, a game has been started")

        # Check count
        if len(self.users) < len(self.characters):
            raise AssertionError("There are less players than characters!")

        # Set it
        self._in_game = True


class DbRoom2Character(Base):
    """
        Which character are in use for this room?
    """

    __tablename__ = "room2character"

    _room_id = Integer(name="room_id", args=ForeignKey(DbRoom._id), primary_key=True)
    _room_id.doc = "Room"

    room = relationship("DbRoom")
    room.doc = "Character of Room"

    _character_id = String(name="character_id", args=ForeignKey(DbCharacter._id), primary_key=True)
    _character_id.doc = "Character"

    character = relationship(DbCharacter)
    character.doc = "Character"

    _count = Integer(default=1, info=dict(hidden=True))
    _count.doc = "Characters in use"

    @hybrid_property
    def count(self):
        """
            Characters in use
        """
        return self._count

    @count.setter
    def count(self, value):
        """
            Forbid too less characters for a game (like 0 Merlin)
        """
        if value < self.character.min_count:
            raise AssertionError("Can't decrement value more than the min count")
        self._count = value

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)

        for arg in args:
            if isinstance(arg, DbRoom):
                self._room_id = arg._id
            elif isinstance(arg, DbCharacter):
                self._character_id = arg._id
            else:
                raise ValueError("Bad argument: %s" % type(arg))




