#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/14 下午11:19
# software: PyCharm
# File: Login.py.py

import uiautomator2 as u2
import unittest
import os, re, sys
import time
from CommonModule import Get_SMSRec
from CommonModule import Commonbase
from Common import APP_Device

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

class Login(APP_Device):

    def __init__(self, d, Session ):
        self.d = d
        self.Qu_NewsSess = Session
        self.code_list = []
        # self.get_sms_code_list()
        # self.write_sms_code()

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

    def login(self, Login_number):
        count = 0
        while True:
            count += 1
            if count > 5:
                self.d.make_toast("登录失败次数大于5次，退出执行任务", 5)
                sys.exit("登录失败次数大于5次，退出执行任务")

            if self.Qu_NewsSess(text="我的").exists:
                pass
            else:
                self.back_to_startPage()

            self.Qu_NewsSess(text="我的").click_exists(timeout=2)
            time.sleep(2)

            #
            try:
                self.d(resourceId="com.jifen.qukan:id/q2").click_exists(timeout=3)
                self.d(resourceId="com.jifen.qukan:id/q2").long_click(timeout=3)
            except:
                pass

            # 这里是已经登录, 要先登录的代码
            if self.check_login_stat():
                self.d.make_toast("现在是已经登录状态，开始退出登录，再次使用提供的账号登录", 5)
                self.Qu_NewsSess(scrollable=True).scroll.to(text=unicode("设置", "utf-8"))
                self.Qu_NewsSess(text="设置").click_exists(timeout=5)
                time.sleep(2)
                self.d.watcher("退出登录").when(text="退出登录").click(text="退出登录")
                # self.Qu_NewsSess.click(0.5, 0.97)
                # self.d(text="退出登录").click()
                # self.Qu_NewsSess(text="退出登录").long_click(timeout=3)

                # time.sleep(1)
                # self.d.xpath("//android.widget.Button[@text='退出登录']").click()
                try:
                    self.d(resourceId="com.jifen.qukan:id/q2").long_click(timeout=3)
                except:
                    pass

                self.Qu_NewsSess(text="我的").click_exists(timeout=2)
                try:
                    self.d(resourceId="com.jifen.qukan:id/q2").long_click(timeout=3)
                except:
                    pass


            else:
                self.d.make_toast("现在是未登录状态，开始登录", 5)
                self.d(resourceId="com.jifen.qukan:id/q2").click_exists(timeout=2)
                continue

            # 这里是开始登录的代码
            if Login_number["Type"] == "wechat":

                if self.Qu_NewsSess(text="看资讯就可以赚钱的APP").exists:
                    self.d.click(0.5, 0.43)
                    try:
                        self.d.click(0.5, 0.43)
                        self.d.watcher("Login").when(resourceId="com.jifen.qukan:id/ajt").click()
                        self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ajt").long_click()
                    except:
                        pass

                    time.sleep(2)
                    self.Qu_NewsSess(text="确认登录").click_exists(timeout=2)
                    self.Qu_NewsSess(text="点击领钱").click_exists(timeout=2)

                elif self.Qu_NewsSess(text="社交账号登录").exists:
                    self.d.set_fastinput_ime(True)
                    self.Qu_NewsSess(text="社交账号登录").click_exists(timeout=5)
                    self.Qu_NewsSess(scrollable=True).scroll.to(text=unicode("社交账号登录", "utf-8"))
                    self.Qu_NewsSess.set_fastinput_ime(False)
                    time.sleep(2)
                    self.Qu_NewsSess(text="确认登录").click_exists(timeout=2)
                    self.Qu_NewsSess(text="点击领钱").click_exists(timeout=2)
                else:
                    self.d.make_toast("未进入到微信跳转登录页面", 5)

                self.d(resourceId="com.jifen.qukan:id/q2").click_exists(timeout=2)
                if self.check_login_stat():
                    break
                else:
                    continue

                # # 微信一键登录按钮 ajt
                # if self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ajt").exists:
                #     self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ajt").long_click()
                #     time.sleep(2)
                #     self.Qu_NewsSess(text="确认登录").click_exists(timeout=2)
                #     self.Qu_NewsSess(text="点击领钱").click_exists(timeout=2)
                #     if self.check_login_stat():
                #         break
                #     else:
                #         continue
                # else:
                #     self.d.make_toast("未进入到微信跳转登录页面", 5)

            elif Login_number["Type"] == "Phone":
                if self.Qu_NewsSess(text="请输入11位手机号码").exists:
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/adj").clear_text()
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/adj").set_text(Login_number["Phone"])
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ix", text="获取短信验证码").click_exists(timeout=5)
                    time.sleep(2)
                    self.Qu_NewsSess(text="确认登录").click_exists(timeout=2)
                    self.Qu_NewsSess(text="点击领钱").click_exists(timeout=2)
                elif self.Qu_NewsSess(text="短信登录").exists:
                    self.Qu_NewsSess(text="短信登录").click_exists(timeout=3)
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/adj").clear_text()
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/adj").set_text(Login_number["Phone"])
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ix", text="获取短信验证码").click_exists(timeout=5)
                    time.sleep(2)
                    self.Qu_NewsSess(text="确认登录").click_exists(timeout=2)
                    self.Qu_NewsSess(text="点击领钱").click_exists(timeout=2)
                else:
                    self.d.make_toast("未进入到微信跳转登录页面", 5)

                self.d(resourceId="com.jifen.qukan:id/q2").click_exists(timeout=2)
                if self.check_login_stat():
                    break
                else:
                    continue

            else:
                self.d.make_toast("登录方法出错，没有你写的登录方法", 5)
                sys.exit("请从新检查登录方法")


    def check_login_stat(self):
        if self.Qu_NewsSess(text="我的").exists:
            pass
        else:
            self.back_to_startPage()
        self.Qu_NewsSess(text="我的").click_exists(timeout=5)
        self.Qu_NewsSess(resourceId="com.jifen.qukan:id/q2").click_exists(timeout=5)

        if self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a6k").exists \
                or self.Qu_NewsSess(scrollable=True).scroll.to(resourceId="com.jifen.qukan:id/a6k"):
            self.d.make_toast("登录成功", 5)
            return True
        else:
            self.d.make_toast("登录失败，正在尝试重新登录", 5)
            return False

    def get_sms_code_list(self):
        self.code_list = list(set(Get_SMSRec.check_codelist('/storage/emulated/0/qpython/scripts3/QuNews/sms.csv')))
        code_present = "获得验证码 %s" % (str(" ".join([str(b) for b in self.code_list])))
        self.d.make_toast(code_present, 5)

    def write_sms_code(self):
        try:
            if self.d(resourceId="com.jifen.qukan:id/ip",text="请输入短信验证码").exists:
                for codecontent in self.code_list:
                    for Number in range(codecontent):
                        if Number == 0:
                            self.d(resourceId="com.jifen.qukan:id/is").clear_text()
                            self.d(resourceId="com.jifen.qukan:id/is").set_text(codecontent[Number])
                        elif Number == 1:
                            self.d(resourceId="com.jifen.qukan:id/it").clear_text()
                            self.d(resourceId="com.jifen.qukan:id/it").set_text(codecontent[Number])
                        elif Number == 2:
                            self.d(resourceId="com.jifen.qukan:id/iu").clear_text()
                            self.d(resourceId="com.jifen.qukan:id/iu").set_text(codecontent[Number])
                        elif Number == 3:
                            self.d(resourceId="com.jifen.qukan:id/iv").clear_text()
                            self.d(resourceId="com.jifen.qukan:id/iv").set_text(codecontent[Number])
                        else:
                            self.d.make_toast("验证码输入错误", 5)
            else:
                self.d.make_toast("没有到达输入验证码页面", 5)
        except:
            if self.d(resourceId="com.jifen.qukan:id/ix",text="请输入短信验证码").exists:
                for codecontent in self.code_list:
                    self.d(resourceId="com.jifen.qukan:id/ix").clear_text()
                    self.d(resourceId="com.jifen.qukan:id/ix").set_text(codecontent)

            else:
                self.d.make_toast("没有到达输入验证码页面", 5)

        if self.d(resourceId="com.jifen.qukan:id/a67").exists:
            try:
                Handle_OtherFrame(self.d).touch_A67()
                print("登录成功")
                self.d.make_toast("登录成功", 5)
                return True
            except :
                return False

        elif self.d(text="我的").exists and self.d(resourceId="com.jifen.qukan:id/vn",text="领取").exists:
            print("登录成功")
            self.d.make_toast("登录成功", 5)
            return True

        else:
            print("登录失败")
            self.d.make_toast("登录失败", 5)
            return False

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
