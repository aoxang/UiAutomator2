#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/7 下午2:51
# software: PyCharm
# File: Read_News.py
import sys
import uiautomator2 as u2
import time
import Login
import random
sys.path.append("/storage/emulated/0/qpython/scripts3/")
from CommonModule.Swipe_class import Swipeclass

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'


def get_header_form_app(d):
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
        # sys.exit("天天快报 新闻阅读失败！ 可能是设备服务未打开。")
    # Login.register(Login_number)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
    else:
        d.press("Home")
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

    My_news_header = []
    if d(className="android.widget.TextView", text="我的频道").exists:
        if d(className="android.view.View").child(resourceId="com.tencent.reading:id/menu_button_txt",
                                                  className="android.widget.TextView").exists:
            count_number = d(className="android.view.View").child(resourceId="com.tencent.reading:id/menu_button_txt",
                                                                  className="android.widget.TextView").count
            for i in range(count_number):
                header = d(className="android.view.View").child(resourceId="com.tencent.reading:id/menu_button_txt",
                                                                className="android.widget.TextView")[i].info["text"]
                if header in My_news_header:
                    continue
                else:
                    My_news_header.append(header)
    # for i in My_news_header:
    #     print i.encode("utf-8")

    other_news_header = {}
    if d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text("更多频道",
                                                                                                              className="android.widget.TextView").exists:
        d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text("更多频道",
                                                                                                               allow_scroll_search=True,
                                                                                                               className="android.widget.TextView").click()
        time.sleep(5)
    else:
        from CommonModule import Swipe_class
        swipe = Swipeclass(d)
        swipe.swipeUp(d, 0.1)
        d(className="android.widget.TextView", text="更多频道",
          resourceId="com.tencent.reading:id/addChannelMoreTxt").click_exists(timeout=5)

    if d(className="android.widget.TextView", text="更多频道", resourceId="com.tencent.reading:id/text_title").exists:
        count_number = d(className="android.widget.ListView",
                         resourceId="com.tencent.reading:id/channel_cat_list_view").child(
            className="android.widget.TextView").count
        for i in range(count_number):
            name = \
                d(className="android.widget.ListView", resourceId="com.tencent.reading:id/channel_cat_list_view").child(
                    className="android.widget.TextView")[i].info["text"]
            d(resourceId="com.tencent.reading:id/channel_cat_list_view").child_by_text(name, allow_scroll_search=True,
                                                                                       resourceId="com.tencent.reading:id/cat_name_text").click()
            countnumber_list = d(className="android.widget.ListView",
                                 resourceId="com.tencent.reading:id/channel_list_view").child(
                className="android.widget.TextView", resourceId="com.tencent.reading:id/channel_name").count
            if name in other_news_header:
                continue
            other_news_header[name] = []
            for k in range(countnumber_list):
                name_list = \
                    d(className="android.widget.ListView", resourceId="com.tencent.reading:id/channel_list_view").child(
                        className="android.widget.TextView", resourceId="com.tencent.reading:id/channel_name")[k].info[
                        "text"]
                other_news_header[name].append(name_list)
    # for key, value in other_news_header.items():
    #     for i in value:
    #         print key.encode("utf-8"), i.encode("utf-8")
    d = backtohome(d)
    return My_news_header, other_news_header


def detect_app_start(d):
    try:
        if d(resourceId="com.tencent.reading:id/nav_btn", className="android.widget.ImageView").exists:
            d(resourceId="com.tencent.reading:id/nav_btn", className="android.widget.ImageView").click_exists(timeout=3)
            print("天天快报 App 正在home桌面.")
            return 0
    except:
        d.healthcheck()
        d = u2.connect('http://0.0.0.0:7912')
        time.sleep(1)
        d.app_stop('com.tencent.reading')
        time.sleep(2)
        d.app_start('com.tencent.reading')
        time.sleep(5)
        d.make_toast("重新启动天天快报App", 3)
        if d(text=u"Continue").exists:
            d(text=u"Continue").click_exists(timeout=5)
        elif d(text=u"CONTINUE").exists:
            d(text=u"CONTINUE").click_exists(timeout=5)
        elif d(text=u"跳过").exists:
            d(text=u"跳过").click_exists(timeout=5)
        else:
            d.make_toast("App启动失败", 3)
            sys.exit("APP启动失败")
            return 1


def start_app(d, type_detect="normal"):
    time.sleep(1)
    d.press("Home")
    d.app_stop('com.tencent.reading')
    time.sleep(2)
    d.app_start('com.tencent.reading')
    if d(text=u"Continue").exists:
        d(text=u"Continue").click_exists(timeout=5)
    elif d(text=u"CONTINUE").exists:
        d(text=u"CONTINUE").click_exists(timeout=5)
    elif d(text=u"跳过").exists:
        d(text=u"跳过").click_exists(timeout=5)
    for i in range(5):
        d(resourceId="android:id/button1").click_exists(timeout=3)
        d(resourceId="com.tencent.reading:id/text_submit").click_exists(timeout=3)

    time.sleep(2)
    if d(resourceId="com.tencent.reading:id/nav_tv",text="快报").exists:
        pass
    else:
        try:
            d.make_toast("没有检测到天天快到APP，正在安装APP中. ", 10)
            d.app_install('http://dldir1.qq.com/dlomg/chuanyue/kuaibao_63.apk')
            d.app_start('com.tencent.reading')
            time.sleep(2)
            d.disable_popups()
            if d(text=u"Continue").exists:
                d(text=u"Continue").click_exists(timeout=5)
            elif d(text=u"CONTINUE").exists:
                d(text=u"CONTINUE").click_exists(timeout=5)
            elif d(text=u"跳过").exists:
                d(text=u"跳过").click_exists(timeout=5)
            for i in range(5):
                d(resourceId="android:id/button1").click_exists(timeout=3)
                d(resourceId="com.tencent.reading:id/text_submit").click_exists(timeout=3)
        except:
            sys.exit("软件安装出错啦")
    time.sleep(2)

    return d


def start_app_QQ(d, type_detect="normal"):
    time.sleep(1)
    d.press("Home")
    time.sleep(3)
    if type_detect == "login":
        #d.app_clear('com.tencent.mobileqq')
        d.app_stop('com.tencent.mobileqq')
    else:
        d.app_stop('com.tencent.mobileqq')
    time.sleep(3)
    d.app_start('com.tencent.mobileqq')
    time.sleep(10)
    if d(text=u"Continue").exists:
        d(text=u"Continue").click_exists(timeout=5)
    elif d(text=u"CONTINUE").exists:
        d(text=u"CONTINUE").click_exists(timeout=5)
    elif d(text=u"跳过").exists:
        d(text=u"跳过").click_exists(timeout=5)
    d.make_toast("启动QQ成功", 3)
    return d


def backtohome(d):
    try:
        for n in range(7):
            d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=2)
    except:
        pass
    return d


def Read_Headers(d):
    My_news_header, other_news_header = get_header_form_app(d)
    time.sleep(3)
    print My_news_header
    print other_news_header
    d.make_toast(str(My_news_header), 5)
    time.sleep(5)
    d.make_toast(str(other_news_header), 5)
    time.sleep(5)
    print "Finished!"
    d.make_toast("done by liaoshengyou", 1)
    return My_news_header, other_news_header

def Read_News(d, My_news_header):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
        # sys.exit("天天快报 新闻阅读失败！ 可能是设备服务未打开。")
    # Login.register(Login_number)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
    else:
        backtohome(d)
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

    d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
        My_news_header, allow_scroll_search=True, className="android.widget.TextView").click()

    paper_number = 0
    for i in range(50):
        count_number = d(resourceId="com.tencent.reading:id/home_viewpager",
                         className="android.support.v4.view.ViewPager").child(
            resourceId="com.tencent.reading:id/top_group_ll").count
        for k in range(1, count_number - 1):
            if d(className="android.widget.FrameLayout").child(className="android.widget.LinearLayout").child(
                    text="精选").exists:
                pass
            else:
                backtohome(d)
                swipe = Swipeclass(d)
                stats = detect_app_start(d)
                if stats == 0:
                    pass
                else:
                    d = start_app(d)
                time.sleep(3)
                if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
                else:
                    backtohome(d)
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

                d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
                    My_news_header, allow_scroll_search=True, className="android.widget.TextView").click_exists(
                    timeout=3)

            if \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/big_video_mask").exists:
                d.make_toast("阅读视频 ", 1)
                d(resourceId="com.tencent.reading:id/home_viewpager",
                  className="android.support.v4.view.ViewPager").child(
                    resourceId="com.tencent.reading:id/top_group_ll")[k].click()
                # contentDescription = d(resourceId="com.tencent.reading:id/home_viewpager",className="android.support.v4.view.ViewPager").child(resourceId="com.tencent.reading:id/top_group_ll")[k].info["contentDescription"]
                # d.make_toast(contentDescription, 1)
                time.sleep(random.randint(15, 30))
                # d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                # d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                # time.sleep(random.randint(16, 25))
                # d(scrollable=False).scroll.toEnd() #拽到底部
                # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                # swipe.swipeUp(d, 0.001) #juet 0.85-0.25
                if d(resourceId="com.tencent.reading:id/drawer_layout").child(
                        className="android.widget.ImageView").exists:
                    time.sleep(random.randint(1, 3))
                # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮
                paper_number += 1
                d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)

            elif \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/video_flag").exists:
                d.make_toast("阅读视频 ", 1)
                d(resourceId="com.tencent.reading:id/home_viewpager",
                  className="android.support.v4.view.ViewPager").child(
                    resourceId="com.tencent.reading:id/top_group_ll")[k].click()
                # contentDescription = d(resourceId="com.tencent.reading:id/home_viewpager",className="android.support.v4.view.ViewPager").child(resourceId="com.tencent.reading:id/top_group_ll")[k].info["contentDescription"]
                # d.make_toast(contentDescription, 1)
                time.sleep(random.randint(15, 30))
                # d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                # d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                # time.sleep(random.randint(16, 25))
                # d(scrollable=False).scroll.toEnd() #拽到底部
                # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                # swipe.swipeUp(d, 0.001) #juet 0.85-0.25
                if d(resourceId="com.tencent.reading:id/drawer_layout").child(
                        className="android.widget.ImageView").exists:
                    time.sleep(random.randint(1, 3))
                # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮
                paper_number += 1
                d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)

            else:
                if d(resourceId="com.tencent.reading:id/home_viewpager",
                     className="android.support.v4.view.ViewPager").child(
                    resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                    resourceId="com.tencent.reading:id/list_title_text").exists:
                    d.make_toast("阅读新闻 ", 1)
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].click()
                    # contentDescription = d(resourceId="com.tencent.reading:id/home_viewpager",className="android.support.v4.view.ViewPager").child(resourceId="com.tencent.reading:id/top_group_ll")[k].info["contentDescription"]
                    # d.make_toast(contentDescription, 1)
                    time.sleep(2)
                    d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                    d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                    time.sleep(random.randint(16, 25))
                    # d(scrollable=False).scroll.toEnd() #拽到底部
                    # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                    # swipe.swipeUp(d, 0.001) #juet 0.85-0.25
                    if d(resourceId="com.tencent.reading:id/drawer_layout").child(
                            className="android.widget.ImageView").exists:
                        time.sleep(2)
                    # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮
                    paper_number += 1
                    d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)
                else:
                    continue

            if paper_number >= 1800:
                break
        print(i)
        # d(scrollable=False).scroll(steps=100)
        swipe.swipeUp(d, random.uniform(0.001, 2.0))
        # d(text="Settings").drag_to(0.5, 0.12, duration=0.5)
        time.sleep(random.randint(1, 10))

    print("Read News Done !")
    d.make_toast("Read News Done !", 2)
    return d


def Do_Red_Task_Reading_Paper(d, My_news_header, paper_number):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
    else:
        backtohome(d)
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

    d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
        My_news_header, allow_scroll_search=True, className="android.widget.TextView").click()

    paper_count = 0
    for i in range(paper_number * 2):
        count_number = d(resourceId="com.tencent.reading:id/home_viewpager",
                         className="android.support.v4.view.ViewPager").child(
            resourceId="com.tencent.reading:id/list_title_text").count
        for k in range(1, count_number):
            if d(className="android.widget.FrameLayout").child(className="android.widget.LinearLayout").child(
                    text="精选").exists:
                pass
            else:
                backtohome(d)
                swipe = Swipeclass(d)
                stats = detect_app_start(d)
                if stats == 0:
                    pass
                else:
                    d = start_app(d)
                time.sleep(3)
                if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
                else:
                    backtohome(d)
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

                d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
                    My_news_header, allow_scroll_search=True, className="android.widget.TextView").click_exists(
                    timeout=3)

            if \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/big_video_mask").exists:
                continue

            elif \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/video_flag").exists:
                continue
            elif \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/small_tips").exists:
                continue
            else:
                d(resourceId="com.tencent.reading:id/home_viewpager",
                  className="android.support.v4.view.ViewPager").child(
                    resourceId="com.tencent.reading:id/top_group_ll")[k].click_exists(timeout=3)
                if d(className="android.widget.ImageView").exists:
                    time.sleep(2)
                    d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                    d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                    time.sleep(random.randint(16, 25))
                    # d(scrollable=False).scroll.toEnd() #拽到底部
                    # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                    # swipe.swipeUp(d, 0.001) #juet 0.85-0.25
                    if d(resourceId="com.tencent.reading:id/drawer_layout").child(
                            className="android.widget.ImageView").exists:
                        time.sleep(2)
                    # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮
                    paper_count += 1
                    d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)
                else:
                    d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)

                '''
                if d(resourceId="com.tencent.reading:id/home_viewpager", className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                    resourceId="com.tencent.reading:id/big_video_mask").exists:
                    continue
    
                elif d(resourceId="com.tencent.reading:id/home_viewpager", className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                    resourceId="com.tencent.reading:id/video_flag").exists:
                    continue
                elif (resourceId="com.tencent.reading:id/home_viewpager", className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                    resourceId="com.tencent.reading:id/small_tips").exists:
                    continue
                else:
                    if d(resourceId="com.tencent.reading:id/home_viewpager",
                         className="android.support.v4.view.ViewPager").child(
                            resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/list_title_text").exists:
                        d.make_toast("阅读新闻 ", 1)
                        d(resourceId="com.tencent.reading:id/home_viewpager",
                          className="android.support.v4.view.ViewPager").child(
                            resourceId="com.tencent.reading:id/top_group_ll")[k].click()
                        time.sleep(2)
                        d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                        d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                        time.sleep(random.randint(16, 25))
                        # d(scrollable=False).scroll.toEnd() #拽到底部
                        # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                        # swipe.swipeUp(d, 0.001) #juet 0.85-0.25
                        if d(resourceId="com.tencent.reading:id/drawer_layout").child(
                                className="android.widget.ImageView").exists:
                            time.sleep(2)
                        # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮
                        paper_number += 1
                        d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)
                    else:
                        continue
                    '''

        if paper_count >= paper_number:
            break
        print(i)
        # d(scrollable=False).scroll(steps=100)
        swipe.swipeUp(d, random.uniform(0.001, 2.0))
        # d(text="Settings").drag_to(0.5, 0.12, duration=0.5)
        time.sleep(random.randint(1, 10))
    print("Read News Done !")
    d.make_toast("Read News Done !", 2)
    return d


def Do_Red_Task_Reading_and_share_Paper(d, My_news_header, paper_number):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
    else:
        backtohome(d)
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

    d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
        My_news_header, allow_scroll_search=True, className="android.widget.TextView").click_exists(timeout=3)

    paper_count = 0
    for i in range(paper_number * 2):
        count_number = d(resourceId="com.tencent.reading:id/home_viewpager",
                         className="android.support.v4.view.ViewPager").child(
            resourceId="com.tencent.reading:id/list_title_text").count
        for k in range(1, count_number):
            if d(className="android.widget.FrameLayout").child(className="android.widget.LinearLayout").child(
                    text="精选").exists:
                pass
            else:
                backtohome(d)
                swipe = Swipeclass(d)
                stats = detect_app_start(d)
                if stats == 0:
                    pass
                else:
                    d = start_app(d)
                time.sleep(3)
                if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
                else:
                    backtohome(d)
                    d(className="android.widget.ImageView",
                      resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

                d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
                    My_news_header, allow_scroll_search=True, className="android.widget.TextView").click_exists(
                    timeout=3)

            if \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/big_video_mask").exists:
                continue

            elif \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/video_flag").exists:
                continue
            elif \
                    d(resourceId="com.tencent.reading:id/home_viewpager",
                      className="android.support.v4.view.ViewPager").child(
                        resourceId="com.tencent.reading:id/top_group_ll")[k].child(
                        resourceId="com.tencent.reading:id/small_tips").exists:
                continue
            else:
                d(resourceId="com.tencent.reading:id/home_viewpager",
                  className="android.support.v4.view.ViewPager").child(
                    resourceId="com.tencent.reading:id/top_group_ll")[k].click_exists(timeout=3)
                if d(className="android.widget.ImageView").exists:
                    time.sleep(2)
                    d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                    d(scrollable=False).fling.toEnd(random.randint(30, 80))  # 飞到底部
                    time.sleep(random.randint(5, 15))
                    # d(scrollable=False).scroll.toEnd() #拽到底部
                    # d(scrollable=False).scroll.toBeginning(steps=50) #拽到开头
                    # swipe.swipeUp(d, 0.001) #juet 0.85-0.25

                    # d(scrollable=False).scroll.to(text=unicode("点赞", "utf-8"))  # 自动滑动找到点赞按钮

                    ''' #评论
                    d(resourceId="com.tencent.reading:id/btn_input").click_exists(timeout=3)
                    d(resourceId="com.tencent.reading:id/input").clear_text()
                    d(resourceId="com.tencent.reading:id/input").set_text(share_content)
                    if k == andom.randint(1, 4):
                        d(resourceId="com.tencent.reading:id/emotion_toggle_view").click_exists(timeout=3)
                        d(resourceId="com.tencent.reading:id/emoji", text=u"😌").click_exists(timeout=3)
                    d(resourceId="com.tencent.reading:id/btn_send").click_exists(timeout=3)
                    '''

                    d(resourceId="com.tencent.reading:id/writing_comment_share").click_exists(timeout=3)
                    d(resourceId="com.tencent.reading:id/share_icon_container").click_exists(timeout=3)
                    if d(scrollable=False).scroll.to(text=u"廖声友"):
                        d(scrollable=False).scroll.to(text=u"廖声友")
                        d(resourceId="com.tencent.mobileqq:id/text1", text=u"廖声友").click()
                    else:
                        d(resourceId="com.tencent.mobileqq:id/title", className="android.view.View", instance=3).click()
                    d(resourceId="com.tencent.mobileqq:id/dialogRightBtn").click()
                    d(resourceId="com.tencent.mobileqq:id/dialogLeftBtn", text="返回天天快报").click_exists(timeout=5)
                    paper_count += 1
                    d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)
                else:
                    d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=3)

        if paper_count >= paper_number:
            break
        print(i)
        # d(scrollable=False).scroll(steps=100)
        swipe.swipeUp(d, random.uniform(0.001, 2.0))
        # d(text="Settings").drag_to(0.5, 0.12, duration=0.5)
        time.sleep(random.randint(1, 10))
    print("Shared News Done !")
    d.make_toast("Shared News Done !", 2)
    return d


def Do_Red_Task_Reading_4_small_video(d, video_number, shared="no"):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
    time.sleep(3)
    if d(resourceId="com.tencent.reading:id/nav_tv", className="android.widget.TextView", text=u"小视频").exists:
        d(resourceId="com.tencent.reading:id/nav_tv", className="android.widget.TextView", text=u"小视频").click()
    else:
        backtohome(d)
        d(resourceId="com.tencent.reading:id/nav_tv", className="android.widget.TextView", text=u"小视频").click_exists(
            timeout=3)
    paper_count = 0
    for i in range(video_number * 2):
        if d(resourceId="com.tencent.reading:id/welfare_anim").exists:
            for k in range(4):
                time.sleep(random.randint(15, 22))
                swipe.swipeUp(d, 0.01)
                # d(scrollable=False).scroll(steps=random.randint(100, 120))  # just a screen
                if shared and k == random.randint(1, 4):
                    d(resourceId="com.tencent.reading:id/discover_video_share_iv").click()
                    d(resourceId="com.tencent.reading:id/share_icon").click_exists(timeout=3)
                    if d(scrollable=False).scroll.to(text=u"廖声友"):
                        d(scrollable=False).scroll.to(text=u"廖声友")
                        d(resourceId="com.tencent.mobileqq:id/text1", text=u"廖声友").click()
                    else:
                        d(resourceId="com.tencent.mobileqq:id/title", className="android.view.View", instance=3).click()
                    d(resourceId="com.tencent.mobileqq:id/dialogRightBtn").click()
                    d(resourceId="com.tencent.mobileqq:id/dialogLeftBtn", text="返回天天快报").click_exists(timeout=5)
            paper_count += 1
        if paper_count >= video_number:
            break
        print(i)
        time.sleep(random.randint(1, 10))

    d(resourceId="com.tencent.reading:id/nav_tv", className="android.widget.TextView", text=u"快报").click()
    print("Reading video Done !")
    d.make_toast("Reading video Done !", 2)
    return d


def Do_Red_Task_Reading_long_video(d, My_news_header, video_number):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)
    else:
        backtohome(d)
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/title_right").click_exists(timeout=3)

    d(className="android.widget.ScrollView", resourceId="com.tencent.reading:id/scrollView").child_by_text(
        My_news_header, allow_scroll_search=True, className="android.widget.TextView").click()

    for i in range(video_number * 2):
        d(resourceId="com.tencent.reading:id/play_bg").click()
        time.sleep(25)
        # swipe.swipeUp(d, 1)
        d(scrollable=False).scroll(steps=random.randint(100, 120))
        time.sleep(random.randint(1, 10))
    print("Reading Long Vedio Done !")
    d.make_toast("Reading Long Vedio Done !", 2)
    return d


def Do_Red_Task_Qiandao_and_ShaiyiShai(d, Login_number):
    backtohome(d)
    swipe = Swipeclass(d)
    stats = detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = start_app(d)
        # sys.exit("天天快报 新闻阅读失败！ 可能是设备服务未打开。")
    # Login.register(Login_number)
    time.sleep(3)
    if d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/user_icon").exists:
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/user_icon").click_exists(timeout=3)
    else:
        d.press("Home")
        d(className="android.widget.ImageView", resourceId="com.tencent.reading:id/user_icon").click_exists(timeout=3)

    if d(className="android.widget.RelativeLayout", resourceId="com.tencent.reading:id/game_entry").exists:
        d(className="android.widget.RelativeLayout", resourceId="com.tencent.reading:id/game_entry").click_exists(
            timeout=3)
    else:
        d(className="android.support.v7.widget.RecyclerView").child_by_text("福利红包", allow_scroll_search=True,
                                                                            resourceId="com.tencent.reading:id/mine_tab_better_normal_entry_name").click()

    time.sleep(2)  # in order to open the redbag website
    if d(description=u"立即签到", className="android.view.View").exists:
        d(description=u"立即签到", className="android.view.View").click_exists(timeout=5.0)
        d(description=u"知道了", className="android.view.View").click_exists(timeout=3.0)
    else:
        pass

    d(scrollable=False).scroll.to(description=u"日常任务")
    d(description=u"日常任务").drag_to(resourceId="com.tencent.reading:id/text_title", className="android.widget.TextView",text="福利红包", duration=0.25)

    if d(className="android.widget.ListView").child(className="android.widget.Button")[0].info[
        "contentDescription"] == "已完成":
        pass
    if d(className="android.widget.ListView").child(className="android.widget.Button")[0].info[
        "contentDescription"] == "去签到":
        d(className="android.widget.ListView").child(className="android.widget.Button")[0].click()
        pass
    if d(className="android.widget.ListView").child(className="android.widget.Button", description="晒一晒").exists:
        shai_shouru(d)
    return d


def shai_shouru(d):
    d(className="android.widget.ListView").child(className="android.widget.Button", description="晒一晒").click_exists(
        timeout=5)
    for k in range(6):
        print(k)
        d(resourceId="com.tencent.reading:id/share_icon").click_exists(timeout=5)
        d(className="android.widget.RelativeLayout", instance=9).click()
        d(resourceId="com.tencent.mobileqq:id/dialogRightBtn").click()
        d(resourceId="com.tencent.mobileqq:id/dialogLeftBtn", text="返回天天快报").click_exists(timeout=10)
    return d


if __name__ == '__main__':
    import sys
    import uiautomator2 as u2

    reload(sys)
    sys.setdefaultencoding('utf-8')

    Login_number = {"Type": "QQ", "Phone": "13267126886", "QQ": "532199541", "Code": "521liaoshengyou"}
    d = u2.connect('http://0.0.0.0:7912')
    d = start_app(d, type_detect="login")
    time.sleep(3)
    #d = Login.register(d, Login_number)
    time.sleep(3)
    # d = start_app()
    d.make_toast("天天快报登录完成", 3)
    d = backtohome(d)

    # d = start_app_QQ(d, type_detect="login")
    # if Login.check_qqlogin_stats(d) == 0:
    #     print("QQ 登录成功")
    #     d.make_toast("QQ 登录成功", 3)
    # else:
    #     print("QQ 登录失败")
    #     d.make_toast("QQ 登录成功", 3)
    # time.sleep(3)
    # d = Login.register_for_QQ(d, Login_number)
    # time.sleep(3)

    d = start_app(d)
    d.make_toast("天天快报 晒一晒 开始5次", 3)
    d = Do_Red_Task_Qiandao_and_ShaiyiShai(d, Login_number)
    time.sleep(5)

    d.make_toast("天天快报 阅读新闻 开始10次", 3)
    My_news_header = unicode("精选", "utf-8")
    d = Do_Red_Task_Reading_Paper(d, My_news_header, 10)
    time.sleep(5)

    d.make_toast("天天快报 分享新闻 开始10次", 3)
    My_news_header = unicode("精选", "utf-8")
    d = Do_Red_Task_Reading_and_share_Paper(d, My_news_header, 10)
    time.sleep(5)

    d.make_toast("天天快报 小视频 开始5次", 3)
    My_news_header = unicode("小视频", "utf-8")
    d = Do_Red_Task_Reading_4_small_video(d, 5, shared=True)
    time.sleep(5)

    d.make_toast("天天快报 长视频 开始5次", 3)
    My_news_header = unicode("视频", "utf-8")
    d = Do_Red_Task_Reading_long_video(d, My_news_header, 5)
    time.sleep(5)

    # #My_news_header, other_news_header = Read_Headers(d)
    My_news_header = unicode("推荐", "utf-8")
    d = Read_News(d, My_news_header)
    d.make_toast("测试完成", 5)

    '''
    redbag_task_count = d(className="android.widget.ListView").child(className="android.widget.Button").count
    for k in redbag_task_count:
        if d(className="android.widget.ListView").child(className="android.widget.Button")[k].info["contentDescription"]=="已完成":
            continue
        if d(className="android.widget.ListView").child(className="android.widget.Button")[k].info["contentDescription"]=="去签到":
            d(className="android.widget.ListView").child(className="android.widget.Button")[k].click()

        if d(className="android.widget.ListView").child(className="android.widget.Button").sibling(className="android.view.View",description="晒一晒").exists:
            d(className="android.widget.ListView").child(className="android.widget.Button")[k].click()
    '''

    # d(text="推荐").sibling(className="android.widget.TextView")[2].info["text"]
    # d(className="android.widget.LinearLayout").child_by_text("高级设置",allow_scroll_search=True)
    # d(className="android.widget.LinearLayout").child(className="android.widget.TextView")[0].info["text"]
    # d(className="android.widget.ListView", resourceId="android:id/list").child_by_text("蓝牙",className="android.widget.LinearLayout").click()
    # d(className="android.widget.ListView", resourceId="android:id/list").child_by_text("关于手机",allow_scroll_search=True,className="android.widget.LinearLayout").click()
