#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/20 上午12:36
# software: PyCharm
# File: Commonbase.py

import uiautomator2 as u2
import unittest
import logging
logging.basicConfig(level=logging.INFO, format=\
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os, re, sys


PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

class Base:
    def __init__(self):
        self.d = u2.conntect(id)
        self.d.app_start(packagename)

    def find_element(self, element):
        '''
        :param self:
        :param element:  元素名称/定位方式
        :return:
        '''
        logger.info("查找元素:{}".format(element))
        if str(element).startswith("com."):
            return self.d(resourceId=element)
        elif re.findall("//",str(element)):
            return self.d.path(element)
        else:
            return self.d(text=element)

    def click(self, element):
        self.find_element(element).click()
        logger.info("点击元素:{}".format(element))





class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
