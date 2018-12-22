#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/14 下午11:08
# software: PyCharm
# File: __init__.py.py

import uiautomator2 as u2
import unittest
import os, re, sys
import subprocess, threading, json, time, datetime, json, random, requests
import urllib
import pymysql
from public import Swipeclass
from public import Hproseclass
import multiprocessing
from multiprocessing import Pool, Lock

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

uiautomator2.DEBUG = True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
