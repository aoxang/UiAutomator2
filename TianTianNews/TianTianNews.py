#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/1 下午9:58
# software: PyCharm
# File: TianTianNews.py.py

import re
import subprocess
import time
from multiprocessing import Pool
import Login

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

uiautomator2.DEBUG = True
devices_list = []

# 获取设备序列号以及设备数量
def finddevices():
    data = subprocess.Popen('adb devices', stdout=subprocess.PIPE, universal_newlines=True)
    data_info = data.stdout.read()
    devices = re.findall(r'(.*?)\s+device', data_info)
    if len(devices) > 1:
        deviceIds = devices[1:]
        print('共找到%s个手机' % str(len(devices) - 1))
        for i in deviceIds:
            devices_list.append(i)
            print('ID为%s' % i)
        return deviceIds
    else:
        print('没有找到手机，请检查')
        raise Exception(u" No devices Found! ")
        #exit("No devices Found!")


if __name__ == '__main__':
    PLATFORM = 'Android 5.0'
    deviceName = 'OPPO A37m'
    app_package = 'com.tencent.reading'
    app_activity = '.ui.LauncherUI'
    driver_server = 'http://0.0.0.0:7912'
    time_start = time.time()
    finddevices()
    # group_names_list = []
    print("""
            请选择:
            1.helper
            
            2.登录天天快报账号
            
            3.阅读文章刷积分
            
            4.阅读视频刷积分
            
            5.点赞
            
            6.分享
            
            7.积分兑支付宝
        """)

    # num2 = int(input('请输入同时执行机器的数量: '))
    # num1 = int(input('请输入数量: '))
    # number = int(input('请输入任务编号: '))
    if number == 1:
        mission = Login.register(Login_number = {"Type": "QQ", "Phone": "13267126886", "QQ": "532199541", "Code": "521liaoshengyou"})
    elif number == 2:
        mission = Login.register(Login_number = {"Type": "QQ", "Phone": "13267126886", "QQ": "532199541", "Code": "521liaoshengyou"})
    elif number == 3:
        mission = xm_time_line.like
    elif number == 4:
        mission = xm_invited_group.invited
    elif number == 5:
        mission = xm_add_group.search
    pool = Pool(num2)
    for x in range(len(devices_list)):
        # group_names = xm_module.test_string(file_path='groups.txt')[x * 50: x * 50+50]
        pool.apply_async(func=mission, args=(num1, devices_list[x]))
    pool.close()
    pool.join()
    time_end = time.time()
    print('%.1f' % (time_end - time_start))
    print('所有任务已结束!')
    pool.terminate()


