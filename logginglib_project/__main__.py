#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/5/18
# author:      he.zhiming
#

"""
本文件描述:
"""

from __future__ import unicode_literals, absolute_import

import sys
import time

from logginglib_project.common_libs import log_factory
from .business_layer import core


def test_func(a, b):
    """this is the doc string

    :param a:
    :param b:
    :return:
    """
    # pylint: disable=invalid-name,logging-not-lazy
    log_factory.DEBUGGER.info('==== test_func start. args is: %s====' % [a, b])

    time.sleep(3)
    log_factory.DEBUGGER.info('RUNNING')

    log_factory.DEBUGGER.info('START CALL FUNCTION')
    result = core.CoreUtils.get_hellowolrd()
    log_factory.DEBUGGER.info('GOT RESULT. %s' % [result, ])

    log_factory.DEBUGGER.info('WILL RETURN VALUE.')
    return 42


def main():
    """doc string

    :return:
    """
    test_func(1, 10)

    return 0


if __name__ == '__main__':
    sys.exit(main())
