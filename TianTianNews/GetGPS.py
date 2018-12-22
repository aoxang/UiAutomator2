#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/7 上午1:14
# software: PyCharm
# File: GetGPS.py.py

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'


# -*- coding: utf-8 -*-
import androidhelper
import time

droid = androidhelper.Android()
droid.startSensingTimed(1, 250)
droid.startLocating()

while 1:
    gpsdata = droid.readLocation().result
    s6data = droid.sensorsReadOrientation().result
    if len(gpsdata)>0:
        print gpsdata['gps']['bearing'] #取得Gps导向(bearing)(角度)
    if len(s6data)>0:
        print s6data[0] #取得罗盘方位角(azimuth)(弧度)
    time.sleep(0.5)

droid.stopLocating()
droid.stopSensing()

