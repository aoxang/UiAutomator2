#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/14 下午11:25
# software: PyCharm
# File: Common.py.py

import sys
import os
import re
sys.path.append("/storage/emulated/0/qpython/scripts3")
import threading
import time
# from CommonModule import Swipe_class
# from CommonModule import Hproseclass
from CommonModule import BackToNormal
from CommonModule import Get_SMSRec
import logging
logging.basicConfig(level=logging.INFO, format=\
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

class APP_Device:
    def __init__(self, d, package=None):
        self.d = d
        self.package = package
        self.code_list = []
        # self.get_sms_code_list()
        # self.write_sms_code()
        self.Qu_NewsSess = d.session()
        if package:
            print("Please Start APP Now!")
        else:
            print("Please Provide a APP name.")

    def start_app(self):
        # self.d.healthcheck()
        while True:
            for i in range(2):
                self.d.press("home")
            self.d.app_stop(self.package)

            # self.d.app_start(self.package)
            try:
                self.Qu_NewsSess = self.d.session(self.package)
                self.Qu_NewsSess(text="以后更新").click_exists(timeout=2)
            except:
                self.install_app()
                self.start_app()
                self.Qu_NewsSess = self.d.session(self.package)
                self.Qu_NewsSess(text="以后更新").click_exists(timeout=2)

            for i in range(4):
                self.Qu_NewsSess(text="允许").click_exists(timeout=2)

            time.sleep(1)
            if self.Qu_NewsSess(text=u"先去逛逛").exists:
                self.Qu_NewsSess(text=u"先去逛逛").click_exists(timeout=3)
            elif self.Qu_NewsSess(text=u"Continue").exists:
                self.Qu_NewsSess(text=u"Continue").click_exists(timeout=3)
            elif self.Qu_NewsSess(text=u"CONTINUE").exists:
                self.Qu_NewsSess(text=u"CONTINUE").click_exists(timeout=3)
            elif self.Qu_NewsSess(text=u"跳过").exists:
                self.Qu_NewsSess(text=u"跳过").click_exists(timeout=3)
            elif self.Qu_NewsSess(resourceId="com.jifen.qukan:id/q0").exists:
                self.Qu_NewsSess(text=u"跳过").click_exists(timeout=3)
            else:
                pass

            time.sleep(2)
            if self.Qu_NewsSess(text="我的").exists:
                break
            else:
                self.install_app()
                self.start_app()
        return  self.Qu_NewsSess

    def install_app(self):
        self.d.make_toast("没有检测到天天快到APP，正在安装APP中. ", 10)
        threads = []
        t1 = threading.Thread(target=self.click_popular(), args=(None,))
        threads.append(t1)
        for t in threads:
            t.setDaemon(True)
            t.start()
        self.d.watcher("继续安装").when(text="继续安装").click(text="继续安装")
        self.d.watcher("安装").when(text="安装").click(text="安装")
        self.d.watchers.watched = True
        self.d.app_install('http://apk.1sapp.com/qukan.3.9.1.000.1213.1041001.369.apk')

    def click_popular(self):
        time.sleep(10)
        print("等待app安装弹出的提示框中 30秒开始 ")
        self.d.make_toast("等待app安装弹出的提示框中 30秒开始 ", 30)
        if self.d(text="继续安装").exists:
            self.d(text="继续安装").click_exists(timeout=30)
        elif self.d(text="安装").exists:
            self.d(text="安装").click_exists(timeout=30)
        else:
            print("More Element not detect ")
        print("等待app安装弹出的提示框30秒结束 ")
        self.d.make_toast("等待app安装弹出的提示框30秒结束 ", 5)

    @staticmethod
    def find_element(Qu_NewsSess,element):
        '''
        :param self:
        :param element:  元素名称/定位方式
        :return:
        '''
        logger.info("查找元素:{}".format(element))
        if str(element).startswith("com."):
            return Qu_NewsSess(resourceId=element)
        elif re.findall("//", str(element)):
            return Qu_NewsSess.path(element)
        else:
            return Qu_NewsSess(text=element)

    def back_to_startPage(self):
        while True:
            if self.Qu_NewsSess(text="我的").exists:
                break
            else:
                for i in range(5):
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/gq").click_exists(timeout=5)
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ii").click_exists(timeout=5)
                    if self.Qu_NewsSess(text="我的").exists:
                        break
                    else:
                        continue
        return True


    def login(self, loginnumber):
        if self.Qu_NewsSess(text="我的").exists:
            self.Qu_NewsSess(text="我的").click_exists(timeout=3)
            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ah3").click_exists(timeout=3)
            self.Qu_NewsSess(text="手机登录").click_exists(timeout=3)
        else:
            self.back_to_startPage()

        if self.Qu_NewsSess(text="请输入11位手机号码").exists:
            self.Qu_NewsSess(text="请输入11位手机号码").clear_text()
            self.Qu_NewsSess(text="请输入11位手机号码").set_text(loginnumber)
            self.Qu_NewsSess(text="获取短信验证码").click_exists(timeout=5)
            self.sent_sms_code()
            return True
        else:
            self.d.make_toast("未进入到登录页面", 5)
            return False

    def Image_recongeic(self):
        if self.d(text="请输入图形验证码").exists:
            self.d(resourceId="com.sohu.inputmethod.sogou:id/imeview_candidates").click_exists(timeout=3)
            try:
                self.d.set_fastinput_ime(True)
            except:
                pass
            imagefile = os.path.join("/storage/emulated/0/qpython/scripts3/QuNews", "imagecode.jpg")
            self.d.screenshot(imagefile)
            #image = Image.open(imagefile)
            #code = pytesseract.image_to_string(image)
            # print image_recongive()
            return code

    # self.get_sms_code_list()
    # self.write_sms_code()

    def get_sms_code_list(self):
        self.code_list = list(set(Get_SMSRec.check_codelist('/storage/emulated/0/qpython/scripts3/QuNews/sms.py')))
        code_present = "获得验证码 %s" % (str(" ".join([str(b) for b in self.code_list])))
        self.d.make_toast(code_present, 5)
        return self.code_list

    def sent_sms_code(self):
        while True:
            time.sleep(7)
            self.code_list = self.get_sms_code_list()
            try:
                if self.Qu_NewsSess(text="请输入短信验证码").exists:
                    for codecontent in self.code_list:
                        for Number in range(codecontent):
                            if Number == 0:
                                self.d(resourceId="com.jifen.qukan:id/is").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/is").set_text(codecontent[Number])
                                self.d(resourceId="com.jifen.qukan:id/im").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/im").set_text(codecontent[Number])
                            elif Number == 1:
                                self.d(resourceId="com.jifen.qukan:id/it").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/it").set_text(codecontent[Number])
                                self.d(resourceId="com.jifen.qukan:id/in").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/in").set_text(codecontent[Number])
                            elif Number == 2:
                                self.d(resourceId="com.jifen.qukan:id/iu").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/iu").set_text(codecontent[Number])
                                self.d(resourceId="com.jifen.qukan:id/io").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/io").set_text(codecontent[Number])
                            elif Number == 3:
                                self.d(resourceId="com.jifen.qukan:id/iv").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/iv").set_text(codecontent[Number])
                                self.d(resourceId="com.jifen.qukan:id/ip").clear_text()
                                self.d(resourceId="com.jifen.qukan:id/ip").set_text(codecontent[Number])
                            else:
                                self.d.make_toast("验证码输入错误", 5)
                else:
                    self.d.make_toast("没有到达输入验证码页面", 5)
            except:
                if self.Qu_NewsSess(text="请输入短信验证码").exists:
                    for codecontent in self.code_list:
                        if self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ix").exists:
                            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ix").clear_text()
                            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ix").set_text(codecontent)
                        elif self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ir").exists:
                            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ir").clear_text()
                            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ir").set_text(codecontent)
                        else:
                            print("找不到地方输入验证码")
                            self.d.make_toast("找不到地方输入验证码", 5)

                else:
                    print("没有到达输入验证码页面")
                    self.d.make_toast("没有到达输入验证码页面", 5)

            if self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a67").exists:
                try:
                    self.touch_a67()
                    print("登录成功")
                    self.d.make_toast("登录成功", 5)
                    break
                    return True
                except:
                    return False
            elif self.Qu_NewsSess(text="我的").exists and self.Qu_NewsSess(text="领取").exists:
                print("登录成功")
                self.d.make_toast("登录成功", 5)
                break
                return True

            elif self.Qu_NewsSess(text="重新发送").exists:
                self.Qu_NewsSess(text="重新发送").click_exists(timeout=5)
                while True:
                    self.write_sms_code()
                break
                return True
            else:
                print("登录失败")
                self.d.make_toast("登录失败", 5)
                continue
                # return False

    def touch_a67(self):
        if self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a67").exists:
            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a67").click_exists(timeout=5)
            time.sleep(3)
            self.back_to_startPage()
        self.d(text="我的").click(timeout=2)

if __name__ == '__main__':
    unittest.main()
