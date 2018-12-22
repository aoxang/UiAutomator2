#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/12/16 上午1:48
# software: PyCharm
# File: Image_ocr.py

import os
from PIL import Image
from ctypes import *
import uiautomator2 as u2
import ctypes

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

# 参数为生成的.so文件所在的绝对路径
libjpeg = cdll.LoadLibrary("/data/local/tmp/libjpgt.so")
libpngt = cdll.LoadLibrary("/data/local/tmp/libpngt.so")
liblept = cdll.LoadLibrary("/data/local/tmp/liblept.so")
libtess = cdll.LoadLibrary("/data/local/tmp/libtess.so")

class tessbaseapi(object):
    def __init__(self):
        self.obj = libtess.tessbaseapi_new()
        # python方法没有参数类型这一选项

    def init(self, datapath, language):
        libtess.init(self.obj, datapath, language)

        # 设置OCR图片

    def SetImage(self, pix):
        libtess.SetImage(self.obj, pix)
        # 得到OCR输出文件

    # def getUTF8Text(self):
    #     return libtess.GetUTF8Text(self.obj)
    #     # 调用时的原来设想就会像下面这样简单了，代码就如下所示了。

    def getUTF8Text(self, outfile, isFileSave):
        libtess.GetUTF8Text(self.obj, outfile)
        with open(outfile, 'r') as f:
            text = f.read().strip()
            if isFileSave != 1:
                os.remove(outfile)
        return text

    # 设置图片模式为单行文本
    def SetPageSegMode_SingleLine(self):
        libtess.SetPageSegMode_SingleLine(self.obj)

    # 设置黑白名单 Eg SetVariable("tessedit_char_blacklist", "xyz"); to ignore x, y and z.
    def SetVariable(self, name, value):
        libtess.SetVariable(self.obj, name, value)

    # 设置OCR范围
    def SetRectangle(self, left, top, width, height):
        libtess.SetRectangle(self.obj, left, top, width, height)


def screen_shot_by_Pillow_grab(x1, y1, x2, y2, outJpeg):
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    # bbox = (760, 0, 1160, 1080)
    bbox = (x1, y1, x2, y2)
    try:
        im = ImageGrab.grab(bbox)
        # 参数 保存截图文件的路径
        im.save(outJpeg)
        return True
    except:
        return False

def screen_shot_by_Pillow_image(x1, y1, x2, y2, outJpeg, d):
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    # bbox = (760, 0, 1160, 1080)
    d.screenshot(outJpeg)
    img = Image.open(outJpeg)
    img = img.crop((x1, y1, x2, y2))
    imagefile = outJpeg + "_crop.png"
    print(imagefile)
    img.save(imagefile)  # format is suffix
    return True

def screen_shot_by_cv2(x1, y1, x2, y2, outJpeg, d):
    import cv2
    try:
        d.screenshot(outJpeg)
        img = cv2.imread(outJpeg)
        print(img.shape)
        corpped = img[y1:y2, x1:x2]  # 裁剪坐标为【y0:y1, x0:x1】
        imagecodefile = outJpeg + "_crop.png"
        cv2.imwrite(imagecodefile, corpped)
        return True
    except:
        return False
        # pytesseract图片识别, 因缺少图片识别的tesseract工具不能使用
        # image = Image.open(imagefile)
        # code = pytesseract.image_to_string(image)
        # print image_recongive()

def recongition_image(x1, y1, x2, y2, Image_Path):
    tess = tessbaseapi()
    os.system("export TESSDATA_PREFIX=$TESSDATA_PREFIX:/storage/emulated/0/qpython/lib/python2.7/site-packages/tessract")
    language = bytes("chi_sim")
    address = bytes("/storage/emulated/0/qpython/lib/python2.7/site-packages/tessract")
    tess.init(address, language)
    img = Image.open(Image_Path)
    img = img.crop((x1, y1, x2, y2))
    imagefile = Image_Path + "_crop.png"
    img.save(imagefile)
    filename = bytes(Image_Path + "_crop.png")
    bitmap = liblept.fopenReadStream(filename)
    content = liblept.pixReadStreamPng(bitmap)
    tess.SetImage(content)
    imagetext = Image_Path + "_code.txt"
    outfile = bytes(imagetext)
    text = tess.getUTF8Text(outfile, 1)
    print(text)
    return text

def main(d, x1_pos, x2_pos, y1_pos, y2_pos, Project_Path):
    # 初始化
    tess = tessbaseapi()
    os.system("export TESSDATA_PREFIX=$TESSDATA_PREFIX:/storage/emulated/0/qpython/lib/python2.7/site-packages/tessract")
    language = bytes("chi_sim")
    address = bytes("/storage/emulated/0/qpython/lib/python2.7/site-packages/tessract")
    tess.init(address, language)

    # 设置图片模式为单行文本
    # tess.SetPageSegMode_SingleLine()
    # tess.SetRectangle(100, 500, 300, 300)

    # # 设置白名单
    # avariable_mode = bytes("tessedit_char_whitelist")
    # whitelist = bytes("abcdedfhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # test = tess.SetVariable(avariable_mode, whitelist)

    # 截取图片
    outJpeg = os.path.join(Project_Path, "imagecode.jpg")
    device_info = d.info  # d.device_info
    Width = int(device_info["displayWidth"])
    Height = int(device_info["displayHeight"])
    x1 = Width*x1_pos
    y1 = Height*y1_pos
    x2 = Width*x2_pos
    y2 = Height*y2_pos
    screen_shot_by_Pillow_image(x1, y1, x2, y2, outJpeg, d)

    # 打开文件，返回FILE*对象
    filename = bytes(outJpeg + "_crop.png")
    bitmap = liblept.fopenReadStream(filename)
    # 转换为PIX*格式型对象
    content = liblept.pixReadStreamPng(bitmap)
    # 设置OCR图片
    tess.SetImage(content)

    # 得到OCR输出文件x
    outTxt = Project_Path + "/imagecode.txt"
    outfile = bytes(outTxt)
    text = tess.getUTF8Text(outfile, 1)
    print(text)
    return text

if __name__ == '__main__':
    d = u2.connect("0.0.0.0:7912")
    Project_Path = "/storage/emulated/0/qpython/scripts3/QuNews/"  # ProJectPath save image code
    x1_pos = 0.242  # Can get it from Weditor cropimage start postion %
    y1_pos = 0.233  # Can get it from Weditor cropimage start postion %
    x2_pos = 0.623  # Can get it from Weditor cropimage end postion %
    y2_pos = 0.304  # Can get it from Weditor cropimage end postion %
    # main(d, x1_pos, x2_pos, y1_pos, y2_pos, Project_Path)
    # print(720*x1_pos, 1280*y1_pos, 720*x2_pos, 1280*y2_pos)
    # recongition_image(720*x1_pos, 1280*y1_pos, 720*x2_pos, 1280*y2_pos, Project_Path+"/imagecode.jpg")
    main(d, x1_pos, x2_pos, y1_pos, y2_pos, Project_Path)
