#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import environment

from sqlalchemy import Column
from sqlalchemy import Unicode as sqUnicode
from sqlalchemy import UnicodeText as sqUnicodeText
from sqlalchemy.orm import composite, CompositeProperty
from base.mutable import MutableObject, MutableComparator

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '13.04.13 - 16:13'


class _i18nObjectComparator(MutableComparator):
    """
        Overwritten for some nice string function support
    """
    pass


class _i18nObject(MutableObject):
    """
        Representation of an translatable text in database
    """
    _fields = environment.langs

    def __str__(self, lang: str=None) -> str:
        if lang not in self._fields:
            raise TypeError("Could not return string representation of _i18nText for lang: %s" % lang)
        return self[lang]


class _i18nPluralizedObject(_i18nObject, MutableObject):
    """
        Representation of an translatable string in database
    """
    _fields = environment.langs + ["%s_pl" % lang for lang in environment.langs]

    def __str__(self, lang: str=None) -> str:
        if lang not in self._fields:
            raise TypeError("Could not return string representation of _i18nString for lang: %s" % lang)
        return self[lang]


def i18nText(name, **kwargs):
    """
        Translatable Text

        :param name: Prefix of the Column
        :param kwargs: Additional Parameters passed to Column Instance

        :rtype: :class:`_i18nObject` as :class:`MutableObject(**environment.langs)`
    """

    dwargs = dict(nullable=False, server_default='')
    dwargs.update(kwargs)

    columns = []

    for lang in environment.langs:
        columns.append(Column('%s_%s' % (name, lang), sqUnicodeText, **dwargs))

    cls = composite(_i18nObject, *columns, comparator_factory=_i18nObjectComparator)
    return cls


def i18nString(name: str, with_plural: bool=False, **kwargs) -> CompositeProperty:
    """
        Translatable String

        Usage:
          >>> news.topic = ('Deutscher Titel', 'English Topic')
          >>> news.topic.en
          'English Topic'
          >>> template.render('{{ _(news.topic) }}')
          'Deutscher Titel'

        :param name: Prefix of column names
        :param with_plural: Does this Column can have a plural?
                            If true, it will generate for each language a \*_pl column additionally.
        :param kwargs: Additional Parameters passed to Column Instance

        :rtype: :class:`_i18nObject` as :class:`MutableObject(**environment.langs)`
    """

    dwargs = dict(nullable=False, server_default='')
    dwargs.update(kwargs)

    columns = []

    for lang in environment.langs:
        columns.append(Column('%s_%s' % (name, lang), sqUnicode, **dwargs))

    if with_plural:
        for lang in environment.langs:
            columns.append(Column('%s_%s_pl' % (name, lang), sqUnicode, **dwargs))

    cls = composite(with_plural and _i18nPluralizedObject or _i18nObject,
                    *columns,
                    comparator_factory=_i18nObjectComparator)
    return cls


