#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from collections import MutableMapping
from sqlalchemy import sql
from sqlalchemy.ext.mutable import MutableComposite
from sqlalchemy.orm import CompositeProperty

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '13.06.13 - 16:20'


class MutableObject(MutableMapping, MutableComposite):
    """
        Representation of an mutable object which attributes are based by _fields

        This behaves pretty like a named tuple with the keywords _fields.
        It additional supports all the requirements to behave as a sqlalchemy r/w composite object
        inclusive dicitonary like access and pickle support.x
    """

    _fields = tuple()

    def __init__(self, *state: tuple):
        MutableMapping.__init__(self)
        MutableComposite.__init__(self)
        try:
            for i, name in enumerate(self._fields):
                setattr(self, name, state[i])
        except IndexError:
            IndexError("Instantiate %s with %u elements, but required are: %s"
                       % (self.__class__.__name__, len(state), self._fields))

    def __composite_values__(self) -> tuple:
        rtn = []
        for i, name in enumerate(self._fields):
            rtn.append(getattr(self, name))
        return tuple(rtn)

    def __getitem__(self, key: str):
        if not key in self._fields:
            raise KeyError("Attribute not known: %s" % str(key))
        return getattr(self, key)

    def __setattr__(self, key: str, value: str):
        object.__setattr__(self, key, value)
        self.changed()

    def __setitem__(self, key: str, value: str):
        if not key in self._fields:
            raise KeyError("Attribute not known: %s" % str(key))
        setattr(self, key, value)

    def __delitem__(self, key: str):
        raise NotImplementedError("%s does not support delitem" % self.__class__.__name__)

    def __eq__(self, other) -> bool:
        for i, name in enumerate(self._fields):
            if getattr(self, name) != getattr(other, name):
                return False
        else:
            return True

    def __ne__(self, other) -> bool:
        for i, name in enumerate(self._fields):
            if getattr(self, name) != getattr(other, name):
                return True
        else:
            return False

    def __getstate__(self) -> tuple:
        state = []
        for i, name in enumerate(self._fields):
            state.append(getattr(self, name))
        return tuple(state)

    def __setstate__(self, state: tuple):
        for i, name in enumerate(self._fields):
            setattr(self, name, state[i])

    def __len__(self) -> int:
        return len(self._fields)

    def __iter__(self):
        for i, name in enumerate(self._fields):
            yield name

    @classmethod
    def coerce(cls, key, value):
        """
            Coerce a value to class

            :param value: value to be coerced
        """
        if hasattr(value, "_fields"):  # DuckType check for named_tuple / MutableMeta
            state = []
            if value._fields != cls._fields:
                ValueError("Coerce an item that does not have the same fields as the mutable meta"
                           " leads to unexpected results")
            for i, name in enumerate(cls._fields):
                state.append(getattr(value, name))
            return cls(*state)
        elif isinstance(value, dict):
            state = []
            for i, name in enumerate(cls._fields):
                if name in value:
                    state.append(value[name])
                else:
                    state.append(None)
            return cls(*state)
        elif isinstance(value, tuple):
            return cls(*value)
        elif not isinstance(value, cls):
            raise ValueError("could not coerce: %s" % type(value))


class MutableComparator(CompositeProperty.Comparator):
    """
        Use this comparator if you want to fallback for your mutable
        for comparision to an any element of comparing
    """

    def like(self, other: str, **kwargs) -> bool:
        """
            Returns true when at least one element like other

            :param other:
        """
        return sql.or_(*[a.like(other) for a in self.__clause_element__().clauses])

    def startswith(self, other: str, **kwargs) -> bool:
        """
            Returns true when at least one element startswith other

            :param other:
        """
        return sql.or_(*[a.startswith(other) for a in self.__clause_element__().clauses])

    def endswith(self, other: str, **kwargs) -> bool:
        """
            Returns true when at least one element endswith other

            :param other:
        """
        return sql.or_(*[a.endswith(other) for a in self.__clause_element__().clauses])