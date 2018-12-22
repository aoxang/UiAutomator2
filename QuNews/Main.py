#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/14 下午11:11
# software: PyCharm
# File: Main.py.py

from Common import *
from Login import *
from Run_task import *
sys.path.append("/storage/emulated/0/qpython/scripts3")

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'


def main():
    Login_number = {"Type": "wechat", "Phone": "13267126886", "QQ": "532199541", "Code": "521liaoshengyou"}
    d = u2.connect('http://192.168.1.16:7912')
    d.jsonrpc.setConfigurator({"waitForIdleTimeout": 100}) # 0
    # print("wait timeout", d.implicitly_wait())
    # d.implicitly_wait(10.0)
    d.device_info
    QuNews = APP_Device(d, package="com.jifen.qukan")
    QuNews_sess = QuNews.start_app()

    #Login(d, QuNews_sess).login(Login_number)

    run = RunTask(d, QuNews_sess)
    run.YuDuZixun()


if __name__ == '__main__':
    import sys
    import uiautomator2 as u2

    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
