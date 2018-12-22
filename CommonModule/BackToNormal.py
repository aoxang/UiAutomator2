#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/15 上午1:27
# software: PyCharm
# File: BackToNormal.py

import uiautomator2 as u2
import unittest

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'


class Android_Fuction(u2.UIAutomatorServer):
    def __init__(self,d):
        self.d =d

    def backToHome(self):
        for i in range(5):
            self.d.press("home")

    def stop_all_app(self):
        self.d.app_stop_all()

    def stop_all_app_exclude(self,App = None):
        if isinstance(App,list):
            pass
        else:
            print("停止APP时给出的APP参数不是List，\
            不能停止APP，请检查后重新运行程序")
            self.d.make_toast("停止APP时给出的APP参数不是List，\
            不能停止APP，请检查后重新运行程序",5)

    def disable_popups(self, enable=True):
        """
        Automatic click all popups
        TODO: need fix
        """
        #raise NotImplementedError()
        # self.watcher
        if enable:
            self.jsonrpc.setAccessibilityPatterns({
                "com.android.packageinstaller":
                [u"确定", u"安装", u"下一步", u"好", u"允许", u"我知道"],
                "com.miui.securitycenter": [u"继续安装"],  # xiaomi
                "com.lbe.security.miui": [u"允许"],  # xiaomi
                "android": [u"好", u"安装"],  # vivo
                "com.huawei.systemmanager": [u"立即删除"],  # huawei
                "com.android.systemui": [u"同意"],  # 锤子
            })
        else:
            self.jsonrpc.setAccessibilityPatterns({})





class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
