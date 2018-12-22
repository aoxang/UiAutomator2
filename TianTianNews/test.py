#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/1 下午9:58
# software: PyCharm
# File: test.py

# -*- coding: utf-8 -*-
import xml.sax
import xml.sax.handler

class XMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping


if __name__ == '__main__':
    xh = XMLHandler()
    xml.sax.parseString(data, xh)
    ret = xh.getDict()

    import pprint

    pprint.pprint(ret)



