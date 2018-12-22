#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/2 上午11:03
# software: PyCharm
# File: Runnning_demo.py

import unittest
import os, re, sys
import multiprocessing
import uiautomator2 as u2
import time, json, random, requests
import urllib
import pymysql

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

packagename = 'com.xx'
activity = 'com.xxx'
packagename_gps = 'com.xxxxx'
activity_gps = 'com.xxxxx'

u2.DEBUG = True

driver = u2.connect('http://192.168.1.2:7912')
#driver = uiautomator2.connect('http://localhost:7912')
driver.app_start(packagename_gps, activity=activity_gps)
time.sleep(5)
driver.app_start(packagename, activity=activity)
time.sleep(5)


def teardown():
    exit_run_module()
    driver.app_stop(packagename)
    driver.app_stop(packagename_gps)

def exit_run_module():
    driver(resourceId='running_button_change_mode_to_normal').click()

    driver(resourceId='pause_button').long_click()

    if driver(resourceId='finish_button').exists:
        driver(resourceId='finish_button').click()
    else:
        raise Exception(u"出错了，没有结束按钮")

    # print self.driver.dump_view()
    driver(text=u'确定').click()

def test_run():
    time.sleep(5)

    if driver(text=u'暂不升级').exists:
        driver(text=u'暂不升级').click()
    driver(text=u'运动').click()
    driver(text=u'户外跑').click()

    if driver(resourceId='running_button_change_mode_to_normal').exists:
        driver(resourceId='running_button_change_mode_to_normal').click()
    else:
        raise Exception(u"出错了，不在跑步地图界面")
    time.sleep(30)

    driver.screenshot('run_end.png')

if __name__ == '__main__':
    test_run()
    teardown()
