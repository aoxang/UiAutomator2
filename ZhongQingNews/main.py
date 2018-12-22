#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/11/21 上午10:29
# software: PyCharm
# File: main.py

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
import Run_JinriNews


PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

uiautomator2.DEBUG = True

def send_code_for_login(d,codelist):
    k = 100
    for i in codelist:
        d(resourceId="com.tencent.reading:id/code_et").clear_text()
        d(resourceId="com.tencent.reading:id/code_et", text="请输入验证码").set_text(i)
        time.sleep(3)

        # d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=5)
        if d(resourceId="com.tencent.reading:id/mine_tab_better_header_user_name").exists:
            print("登录成功")
            k = 0
            break
            return 0
        elif d(resourceId="com.tencent.reading:id/result_tips", text="验证码错误").exists:
            d(resourceId="com.tencent.reading:id/code_et").clear_text()
            continue
        elif d(resourceId="com.tencent.reading:id/result_tips", text="验证码已失效，请重试").exists():
            d(resourceId="com.tencent.reading:id/send_btn", text="重新发送").click_exists(timeout=10)
            new_codelist = list(set(Get_SMSRec.check_codelist()))
            codelist = list(set(new_codelist).difference(set(codelist)))
    if k==0:
        return 0
    else:
        return 1


def check_JinriNews_login_stats(d):
    if d(resourceId="com.ss.android.article.news:id/a4p",className="android.widget.TextView").exists:
        print("登录成功")
        return 0
    else:
        print("登录失败")
        return 1


def detect_JinriNews_app_start(d):
    try:
        if d(resourceId="com.ss.android.article.news:id/cng",className="android.widget.TextView",text="首页").exists:
            d(resourceId="com.ss.android.article.news:id/cng", className="android.widget.TextView", text="首页").click_exists(timeout=3)
            print("虎牙直播 App 正在home桌面.")
            return 0
    except:
        d = u2.connect('http://0.0.0.0:7912')
        time.sleep(1)
        d.press("Home")
        time.sleep(3)
        d.app_stop('com.ss.android.article.news')
        time.sleep(3)
        d.app_start('com.ss.android.article.news')
        time.sleep(5)
        d.make_toast("重新启动 今日头条 App中！", 3)
        if d(text=u"Continue").exists:
            d(text=u"Continue").click_exists(timeout=5)
        elif d(text=u"CONTINUE").exists:
            d(text=u"CONTINUE").click_exists(timeout=5)
        elif d(text=u"跳过").exists:
            d(text=u"跳过").click_exists(timeout=5)
        elif d(description=u'关闭').exists:
            d(description=u'关闭').exists(timeout=5)

        if d(resourceId="com.ss.android.article.news:id/cng",className="android.widget.TextView",text="首页").exists:
            d(resourceId="com.ss.android.article.news:id/cng", className="android.widget.TextView", text="首页").click_exists(timeout=3)
            print("今日头条 App 正在home桌面.")
            d.make_toast("今日头条 App 正在home桌面.", 3)
            return 0
        else:
            d.make_toast("今日头条 App 可能不在桌面.", 3)
            #print("天天快报 App 不在home桌面.")
            return 1

def register(d,Login_number):
    stats = detect_JinriNews_app_start(d)
    try:
        if stats == 0:
            pass
        else:
            d = u2.connect('http://0.0.0.0:7912')
            start_Huya_app(d,type_detect="login")
    except:
        d.make_toast("启动错误，可能是atx-agent服务未打开",3)
        sys.exit("启动错误，可能是atx-agent服务未打开.")

    time.sleep(5)
    #res = d(resourceId = "com.tencent.reading",text = u"天天快报")
    login_stat = 1

    if d(resourceId="ccom.ss.android.article.news:id/cng", text=u"未登录").exists:
        d(resourceId="ccom.ss.android.article.news:id/cng", text=u"未登录").click_exists(timeout=3)
    else:
        Run_Huya.backtohome(d)
        d(resourceId="com.ss.android.article.news:id/cng", text=u"未登录").click_exists(timeout=3)

    if d(resourceId="com.ss.android.article.news:id/bsi",text = "登录").exists:
        d(resourceId="com.ss.android.article.news:id/bsi", text="登录").click_exists(timeout=3)
        d(resourceId="com.ss.android.article.news:id/qj").clear_text()
        if Login_number["Type"]=="Phone":
            d(resourceId="com.ss.android.article.news:id/qj", text="手机号").set_text(Login_number["Phone"])
            #d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=10)
            d(resourceId="com.ss.android.article.news:id/ql", text="请输入验证码" , className="android.widget.EditText").set_text(Login_number["Code"])
        elif Login_number["Type"]=="YY_number":
            d(resourceId="com.ss.android.article.news:id/qj", text="手机号").set_text(Login_number["YY_number"])
            # d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=10)
            d(resourceId="com.ss.android.article.news:id/ql", text="请输入验证码" , className="android.widget.EditText").set_text(Login_number["Code"])
        else:
            d(resourceId="com.ss.android.article.news:id/qj", text="手机号").set_text(Login_number["Phone"])
            # d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=10)
            d(resourceId="com.ss.android.article.news:id/ql", text="请输入验证码" , className="android.widget.EditText").set_text(Login_number["Code"])

        d(resourceId="com.ss.android.article.news:id/q9",text="进入头条").click_exists(timeout=3)
        time.sleep(3)

        login_stat = check_JinriNews_login_stats(d)

    else:
        dd(resourceId="com.ss.android.article.news:id/bsv", text=u"系统设置").click_exists(timeout=3)
        d(className="android.widget.ScrollView", resourceId="com.ss.android.article.news:id/cfs").child_by_text(
            "退出登录", allow_scroll_search=True, className="android.widget.TextView").click()
        d(resourceId="com.ss.android.article.news:id/a7g",text="确认退出").click_exists(timeout=3)
        d(resourceId="com.ss.android.article.news:id/a1").click_exists(timeout=3)
        d(resourceId="com.ss.android.article.news:id/a1").click_exists(timeout=3)


    if login_stat == 1 :
        print("登录失败，请人为手动重新登录.")
        d(resourceId="com.ss.android.article.news:id/cng", text=u"首页").click_exists(timeout=2)
    else:
        print("登录成功")
        d(resourceId="com.ss.android.article.news:id/cng", text=u"首页").click_exists(timeout=2)
        d.make_toast("今日头条 登录成功", 3)

    return d




if __name__ == '__main__':
    #Login_number = {"Type":"Phone","Phone": "13267126886", "QQ":"532199541", "Code": "521liaoshengyou"}
    Login_number = {"Type": "QQ", "Phone": "13267126886", "QQ": "532199541", "Code": "521liaoshengyou"}
    register(Login_number)
