#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/14 下午11:19
# software: PyCharm
# File: Login.py.py



import uiautomator2 as u2
import unittest
import os, re, sys
sys.path.append("/Users/liaoshengyou/Documents/python")
sys.path.append("/Users/liaoshengyou/Documents/python/CommonModule")

import time
from CommonModule import Get_SMSRec
from CommonModule import Commonbase
from Common import APP_Device
from CommonModule.Swipe_class import Swipeclass

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'


class RunTask:

    def __init__(self, d, Session ):
        self.d = d
        self.Qu_NewsSess = Session
        self.code_list = []
        self.Qu_NewsSess(text="任务").click_exists(timeout=5)
        # self.get_sms_code_list()
        # self.write_sms_code()
        self.Newpeoper_task = ["阅读资讯", "查看阅读收益","查看我的钱包","输入邀请码","提现任务","天天领现金"]
        self.Days_task = ["晒晒收入","砸金蛋拿红包","免费拿商品","关注趣头条微信号","开宝箱分享",
                            "累计阅读时长达到60分总","玩游戏疯狂赚金币","轻松赚海量现金",
                            "免费看小说","看小视频", "领分红","试玩领金币","明星推荐"]

    def back_to_startPage(self):
        while True:
            if self.Qu_NewsSess(text="任务").exists:
                break
            else:
                for i in range(5):
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/gq").click_exists(timeout=5)
                    self.Qu_NewsSess(resourceId="com.jifen.qukan:id/ii").click_exists(timeout=5)
                    if self.Qu_NewsSess(text="任务").exists:
                        self.Qu_NewsSess(text="任务").click_exists(timeout=2)
                        break
                    else:
                        continue
        return True

    def Runtasks(self, keys="阅读资讯"):
        if self.Qu_NewsSess(text="任务中心").exists:
            pass
        else:
            self.Qu_NewsSess(text="任务").click_exists(timeout=5)
            self.d.make_toast("现在不在任务中心页面", 5)
            self.back_to_startPage()


        for i in d(text="阅读资讯").sibling(className="android.view.View")



        if self.Qu_NewsSess(text=keys).exists:

            self.Qu_NewsSess.watcher(keys).when(text=keys).click()
            self.Qu_NewsSess(text=keys).click()
            self.Qu_NewsSess(text=keys).click_exists(timeout=5)
            self.Qu_NewsSess(text=keys).long_click(timeout=5)
        else:
            try:
                self.Qu_NewsSess(scrollable=True).scroll.to(text=unicode(keys, "utf-8"))
                self.Qu_NewsSess(text=keys).click_exists(timeout=5)
                self.Qu_NewsSess(scrollable=True).scroll.to(text=unicode("去阅读", "utf-8"))
                self.Qu_NewsSess(text=keys).click_exists(timeout=5)
            except:
                print("没有找到%s" %(keys))

        if self.Qu_NewsSess(text=keys).child_by_text(unicode("已完成", "utf-8")).exists:
            self.d(text="任务").drag_to(text=keys, duration=1)

        i = 0
        count = self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a08").count
        for i in range(count):
            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/a08")[i].click()
            i += 1
            self.Qu_NewsSess(resourceId="com.jifen.qukan:id/vt").click()
            if i >= 2 :
                break
            swipe = Swipeclass(self.Qu_NewsSess)

            time_strat = 1
            while True:
                time_strat += 1
                if time_stratss >= 8:
                    break
                swipe.swipeUp(self.Qu_NewsSess, random.uniform(0.001, 2.0))
                time.sleep(1)

            while True:
                time_strat += 1
                if time_stratss >= 17:
                    break
                swipe.swipeDown(self.Qu_NewsSess, random.uniform(0.001, 2.0))
                time.sleep(1)

            # self.d(scrollable=False).scroll(steps=100)
            # time.sleep(random.randint(1, 17))

        self.back_to_startPage()
        self.Qu_NewsSess(text="任务").click_exists(timeout=5)

        return True


if __name__ == '__main__':
    unittest.main()
