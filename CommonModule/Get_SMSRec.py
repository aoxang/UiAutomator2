#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/6 下午8:42
# software: PyCharm

from androidhelper import Android
import csv
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


def check_code(content):
    #YZMLENGTH = 6
    #regex = re.compile("(?<![0-9])([0-9]{" + YZMLENGTH + "})(?![0-9])",re.I)
    # regex.findall(content)
    regex = re.compile(r"(?<![0-9])([0-9]{4,6})(?![0-9])")

    # pat =  "\d{4,6}(?!\d) " #数字
    # pat = [A - Za - z0 - 9]{4, }(?![A - Za - z0 - 9]) #字母
    #m = re.search(pat,content)
    m = regex.findall(content)
    return m


def check_mail(str):
    pattern = r"\w{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}"
    res = re.findall(pattern, str, re.I)
    return res


def check_qq(str):
    pattern = r"qq:[1-9]\d{4,10}"
    res = re.findall(pattern, str, re.I)
    return res


def check_mobile(strData):
    pattern = r"^1[3-9]\d{9}$"
    res = re.findall(pattern, strData)
    return res


def re_tel(tn):
    reg = "1[3|4|5|7|8][0-9]{9}"
    res = re.findall(reg, tn)
    return res


def check_peoperid(strData):
    pattern = r"^[1-6]\d{5}[12]\d{3}(0[1-9]|1[12])(0[1-9]|1[0-9]|2[0-9]|3[01])\d{3}(\d|X|x)$"
    res = re.match(pattern, strData)
    return res


def write_message(path, sms_data):
    # 将所有短信保存到csv文件中
    names = [
        '_id',
        'address',
        'date',
        'body',
        'read',
        'person',
        'status',
        'type']
    with open(path, 'w') as f:
        # f.write(str(sms_data))
        f_scv = csv.DictWriter(f, names)
        f_scv.writeheader()
        f_scv.writerows(sms_data)


def check_codelist(code_outFile):
    d = Android()
    # 发短信,未成功,qpython3采用sl4a成功
    d.smsSend('10086', 'test')
    # import sl4a
    # droid = sl4a.Android()
    # droid.smsSend("0044....","sms")

    # 获取短信数目
    Message_number = d.smsGetMessageCount(
        False).result  # False表示读取所有短信，True读取未读短信

    # 获取短信id
    Message_ids = d.smsGetMessageIds(True).result
    Message_ids = sorted(Message_ids, reverse=True)
    # print Message_ids

    if len(Message_ids) < 1:
        return []
    else:
        # 获取短信具体内容，默认读取收件箱内容，发送的信息使用参数'sent'
        sms_data = d.smsGetMessages(False, 'inbox').result
        message_body = []
        for message in sms_data:
            #print message["read"],message["type"],message["_id"]
            # if message["read"]!="1":
            if message["read"] != "0":
                continue
            elif message["type"] != "1":
                continue
            else:
                if int(message["_id"]) not in Message_ids[:5]:
                    continue
                else:
                    #print message["body"]
                    code_list = check_code(message["body"])
                    if len(code_list) >= 1:
                        for i in code_list:
                            message_body.append(str(i))
                    # message_body.append(message["body"].decode("unicode_escape"))
                    # message_body.append(message["body"].decode("unicode_escape"))
        write_message(code_outFile, sms_data)
        print message_body
        return message_body


if __name__ == '__main__':
    check_codelist()
