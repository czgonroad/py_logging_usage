#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/6/14
# author:      he.zhiming
#

"""
本文件描述:
"""
from __future__ import unicode_literals, absolute_import

import sys
from unittest import TestCase

from logginglib_project import adder


class Person:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Person(name={p._name})'.format(p=self)

    def __repr__(self):
        return self.__str__()


def geta():
    return 1


def getb():
    return 1


class TestAdder(TestCase):
    def test_add(self):
        a = geta()
        b = getb()

        expected = a + b
        actual = adder.Adder().add(a, b)

        self.assertEqual(expected, actual,
                         msg='%s' % [actual, expected, a, b, ])
