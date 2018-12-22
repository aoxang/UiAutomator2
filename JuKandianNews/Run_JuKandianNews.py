#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/11/21 下午10:11
# software: PyCharm
# File: Run_JinriNews.py

import uiautomator2 as u2
import unittest
import os, re, sys
import subprocess, threading, json, time, datetime, json, random, requests
import urllib
import pymysql
from CommonModule import Swipe_class
from CommonModule import Hproseclass
import multiprocessing
from multiprocessing import Pool, Lock

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

uiautomator2.DEBUG = True



def backtohome(d):
    try:
        for n in range(8):
            d(resourceId="com.ss.android.article.news:id/a1").click_exists(timeout=3)
            if d(resourceId="com.ss.android.article.news:id/abr").exists:
                d(resourceId="com.ss.android.article.news:id/cng", text=u"首页").click_exists(timeout=2)
                break
    except:
        pass
    d(resourceId="com.ss.android.article.news:id/cng", text=u"首页").click_exists(timeout=2)
    return d


def Run_Live(d,Live_number):
    backtohome(d)
    swipe = Swipe_class.Swipeclass(d)
    d(resourceId="com.ss.android.article.news:id/cng", className="android.widget.TextView", text="首页").click_exists(timeout=2)
    live_count = 0
    for e in range(Live_number/6):
        count_number = d(className="android.widget.FrameLayout").child(resourceId="com.duowan.kiwi:id/live_content").count
        for k in range(count_number):
            d(className="android.widget.FrameLayout").child(resourceId="com.duowan.kiwi:id/live_content")[k].click()
            if d(resourceId="com.duowan.kiwi:id/message_tab_subscribe_button").child(
                resourceId="com.duowan.kiwi:id/favor_status").info["text"] == "订阅":
                d(resourceId="com.duowan.kiwi:id/message_tab_subscribe_button").child(
                    resourceId="com.duowan.kiwi:id/favor_status").click()
                d(resourceId="com.duowan.kiwi:id/tv_push_dialog_ignore").click_exists(timeout=3)
            else:
                pass
            #text_content = ["我是琦琦","我是娟娟","我是友友","我在刷弹幕  刷呀刷弹幕"]
            text_content = ["我是娟娟,我在刷弹幕,刷呀刷弹幕","我是琦琦,我在刷弹幕,刷呀刷弹幕"]
            for l in text_content:
                d(resourceId="com.duowan.kiwi:id/chat_edit_container").child(resourceId="com.duowan.kiwi:id/input_edit").set_text(l)
                d(resourceId="com.duowan.kiwi:id/chat_edit_container").child(resourceId="com.duowan.kiwi:id/send_button").click_exists(timeout=3)
                d(resourceId="com.duowan.kiwi:id/tv_agree").click_exists(timeout=5)
                time.sleep(random.randint(2,5))

            d(resourceId="com.duowan.kiwi:id/back_btn").click_exists(timeout=3)
            time.sleep(random.randint(2, 5))
            if d(resourceId="com.duowan.kiwi:id/gl_floating_barrage").exists:
                d(className="android.widget.FrameLayout",).child(resourceId="com.duowan.kiwi:id/floating_close").click_exists(timeout=3)
            d(resourceId="com.duowan.kiwi:id/tv_push_dialog_ignore").click_exists(timeout=3)
            # d(resourceId="com.duowan.kiwi:id/title", text=u"首页").click_exists(timeout=2)

            live_count += 1
            if live_count >= Live_number:
                bread
            else:
                pass

        if live_count >=Live_number:
            bread
        else:
            pass
        # d.make_toast(contentDescription, 1)
        time.sleep(random.randint(15, 30))
        # d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
        # d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
        # time.sleep(random.randint(16, 25))
        # d(scrollable=False).scroll.toEnd() #拽到底部
        # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
        swipe.swipeUp(d, 0.001) #juet 0.85-0.25


    print("刷直播完成 by shengyou")
    return d



if __name__ == '__main__':
    unittest.main()
