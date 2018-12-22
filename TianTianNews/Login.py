#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liaoshengyou
# datetime: 2018/10/6 下午8:42
# software: PyCharm
# File: Login.py

import uiautomator2 as u2
import re
import time
import random
import urllib
from CommonModule import Get_SMSRec
import Read_News

PACKAGE_NAME = 'Liaoshengyou'
VERSION = '0.0.1'
DESCRIPTION = 'Liaoshengyou package'
AUTHOR = 'Liaoshengyou'
LICENSE = 'Copyright 2017 Liaoshengyou.'

'''
db = pymysql.connect(
    host='',
    user='',
    password='',
    port=3306,
    db='',
    use_unicode=True,
    charset=''
)
'''


def send_code_for_login(d, codelist):
    count = 0
    login_stat = False
    while True:
        for i in codelist:
            count+=1
            d(resourceId="com.tencent.reading:id/code_et").clear_text()
            d(resourceId="com.tencent.reading:id/code_et", text="请输入验证码").set_text(i)
            time.sleep(1)

            # d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=5)
            if d(resourceId="com.tencent.reading:id/mine_tab_better_header_user_name").exists:
                d.make_toast("登录成功", 5)
                login_stat = True
                break
            elif d(resourceId="com.tencent.reading:id/result_tips", text="验证码已失效，请重试").exists():
                d(resourceId="com.tencent.reading:id/send_btn",text="重新发送").click_exists(timeout=10)
                new_codelist = list(set(Get_SMSRec.check_codelist()))
                codelist = list(set(new_codelist).difference(set(codelist)))
            elif d(resourceId="com.tencent.reading:id/result_tips", text="验证码错误").exists:
                continue
        if count>=10:
            d.make_toast("验证吗获取太多次数都没有登录成功，退出", 5)
            break

        else:
            continue

    if login_stat:
        return True
    else:
        return False



def check_login_stats(d):
    if d(resourceId="com.tencent.reading:id/mine_tab_better_header_user_name").exists:
        if d(resourceId="com.tencent.reading:id/nav_tv", text=u"未登录").exists:
            print("登录失败")
            return 1
        else:
            print("登录成功")
            return 0
    else:
        print("登录失败")
        return 1


def check_qqlogin_stats(d):
    if d(resourceId="com.tencent.mobileqq:id/conversation_head").exists:
        print("登录成功")
        return 0
    else:
        print("登录失败")
        return 1


def getphone():
    get_url = 'http://api.codedw.com/api/do.php?action=getPhone&token=xxxx&sid=xxxx'
    req = urllib.request.urlopen(get_url)
    print(req)
    ret = req.read()
    ret = ret.decode("UTF-8")
    print(ret)
    data = ret.split('|')
    return data[1]


def getcode(phone):
    time.sleep(5)
    phone = str(phone)
    for i in range(10):
        get_url = "http://api.codedw.com/api/do.php?action=getMessage&token=xxxx&sid=xxxx&phone=%s" % (
            phone)
        req = urllib.request.urlopen(get_url)
        ret = req.read()
        ret = ret.decode("UTF-8")
        print(ret)
        data = ret.split('|')
        code = False
        if data[0] == '1':
            code = data[1]
            print(code)
            code = re.sub(r"\D", "", code)
            break
        else:
            time.sleep(5)
    return code


def rdm(num=6, ty=1):
    salt = ''
    if ty == 1:
        seed = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
        sa = []
        for i in range(num):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
    elif ty == 2:
        index = random.randint(0, 80)
        seed = [
            'Molly',
            'Amy',
            'Claire',
            'Emily',
            'Katie',
            'Medeline',
            'Katelyn',
            'Emma',
            'Abigail',
            'Carly',
            'Jenna',
            'Heather',
            'Katherine',
            'Caitlin',
            'Kaitlin',
            'Holly',
            'Allison',
            'Kaitlyn',
            'Hannah',
            'Kathryn',
            'sarah',
            'emily',
            'jessica',
            'lauren',
            'ashley',
            'amanda',
            'megan',
            'samantha',
            'hannah',
            'rachel',
            'nicole',
            'taylor',
            'elizabeth',
            'katherine',
            'madison',
            'jennifer',
            'alexandra',
            'brittany',
            'danielle',
            'rebecca',
            'macy',
            'maggie',
            'mandy',
            'mango',
            'mani',
            'maple',
            'margie',
            'marsha',
            'maria',
            'mary',
            'may',
            'maya',
            'megan',
            'melissa',
            'michelle',
            'miki',
            'mimi',
            'mona',
            'sally',
            'sammi',
            'sandra',
            'sandy',
            'selina',
            'sara',
            'sarah',
            'serena',
            'shadow',
            'sharon',
            'sheila',
            'sherry',
            'shirley',
            'sky',
            'sophie',
            'stella',
            'stephanie',
            'stephy',
            'jade',
            'janice',
            'jannet',
            'janny',
            'jasmine']
        sa = seed[index]
        salt = ''.join(sa)
    elif ty == 3:
        index = random.randint(0, 12)
        seed = [
            'Richardson',
            'Churchill',
            'Johnson',
            'Smith',
            'Johnson',
            'Williams',
            'Brown',
            'Jones',
            'Miller',
            'Davis',
            'Martinson',
            'Anderson',
            'Wilson']
        sa = seed[index]
        salt = ''.join(sa)
    return salt


def register(d, Login_number):
    stats = Read_News.detect_app_start(d)
    if stats == 0:
        pass
    else:
        d = u2.connect('http://0.0.0.0:7912')

    login_number = 0
    login_stat = False
    while True:
        Read_News.start_app(d, type_detect="login")
        login_number +=1
        d.make_toast('正在启动设备{}'.format(login_number), 3)
        if d(text=u"Continue").exists:
            d(text=u"Continue").click_exists(timeout=3)
        elif d(text=u"CONTINUE").exists:
            d(text=u"CONTINUE").click_exists(timeout=3)
        elif d(text=u"跳过").exists:
            d(text=u"跳过").click_exists(timeout=3)
        elif d(text=u"skip").exists:
            d(text=u"skip").click_exists(timeout=3)
        elif d(text=u"SKIP").exists:
            d(text=u"SKIP").click_exists(timeout=3)
        else:
            pass

        d(resourceId="com.tencent.reading:id/nav_btn", className="android.widget.ImageView").click_exists(timeout=3)

        if d(resourceId="com.tencent.reading:id/mine_tab_better_header_user_name").exists:
            d(resourceId="com.tencent.reading:id/game_entry",
              text=u"设置").click_exists(timeout=3)
            d(resourceId="com.tencent.reading:id/left_desc",
              text="退出登录").click_exists(timeout=3)
            d(text='确定').click_exists(timeout=10)
            if Login_number["Type"] == "Phone" and d(text="手机登录").exists:
                d(text="手机登录").click_exists(timeout=5)
            if Login_number["Type"] == "QQ" and d(text="QQ登录").exists:
                d(text="QQ登录").click_exists(timeout=5)
        else:
            if Login_number["Type"] == "Phone" and d(text="手机登录").exists:
                d(text="手机登录").click_exists(timeout=5)
            elif Login_number["Type"] == "QQ" and d(text="QQ登录").exists:
                d(text="QQ登录").click_exists(timeout=5)
            elif Login_number["Type"] == "Wechat" and d(text="微信登录").exists:
                d(text="微信登录").click_exists(timeout=5)
            else:
                d.make_toast('请提供正确的登录方式，退出中', 3)

        if Login_number["Type"] == "Phone":
            if d(text=u"手机登录").exists:
                d(text=u"手机登录").click_exists(timeout=1)
                d(resourceId="com.tencent.reading:id/phone_number_et").clear_text()
                d(resourceId="com.tencent.reading:id/phone_number_et",
                  text="输入手机号即可快捷登录").set_text(Login_number["Phone"])
                d(resourceId="com.tencent.reading:id/send_btn",
                  text="获取验证码").click_exists(timeout=10)
                time.sleep(10)

            codelist = list(set(Get_SMSRec.check_codelist()))
            temp = "获得验证码 %s" % (str(codelist))
            d.make_toast(temp, 5)

            for resent_number in range(3):
                login_stat = send_code_for_login(d, codelist)
                if login_stat:
                    break
                else:
                    if d(resourceId="com.tencent.reading:id/send_btn", text="重新发送").exists():
                        d(resourceId="com.tencent.reading:id/send_btn", text="重新发送").click_exists(timeout=10)
                        new_codelist = list(set(Get_SMSRec.check_codelist()))
                        codelist = list(set(new_codelist).difference(set(codelist)))
                        login_stat = send_code_for_login(d, codelist)

            if login_stat:
                d.make_toast("登录失败，请人为手动重新登录.", 5)
                d(resourceId="com.tencent.reading:id/btn_share", text="取消").click_exists(timeout=2)
                d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=2)
            else:
                d = Read_News.backtohome(d)
                break

            '''
            d.set_fastinput_ime(True)  # 关闭我们默认的输入法，而使用IME输入法
            d.send_keys("13267126886")
            d.set_fastinput_ime(False)
            d.clear_text()
            '''
            #print('设备{}第{}个注册成功!'.format(services, x + 1))

        elif Login_number["Type"] == "QQ" or Login_number["Type"] == "Wechat":
            d(resourceId="com.tencent.reading:id/nav_btn", className="android.widget.ImageView").click_exists(timeout=3)
            d(text=u"QQ登录").click_exists(timeout=3)
            if d(resourceId="com.tencent.mobileqq:id/name", text=u"授权并登录").exists:
                d(resourceId="com.tencent.mobileqq:id/name", text=u"授权并登录").click_exists(timeout=2)
                if check_login_stats(d) == 0:
                    print "登录成功"
                    login_stat = True
                    break
            elif d(text=Login_number["QQ"]).exists:
                    d(resourceId="com.tencent.mobileqq:id/password").clear_text()
                    d(resourceId="com.tencent.mobileqq:id/password").set_text( Login_number["Code"])
                    # d(description=u"登 录").click_exists(timeout=2)
                    d(resourceId="com.tencent.mobileqq:id/login",
                      description=u"登录").click_exists(timeout=2)
                    time.sleep(5)

            elif d(description="请输入QQ号码或手机或邮箱").exists:
                # d(description="请输入QQ号码或手机或邮箱")
                # d(description="支持QQ号/邮箱/手机号登录").clear_text()
                d(description="请输入QQ号码或手机或邮箱").clear_text()
                d(description="请输入QQ号码或手机或邮箱").set_text(Login_number["QQ"])
                d(resourceId="com.tencent.mobileqq:id/password").clear_text()
                d(resourceId="com.tencent.mobileqq:id/password").set_text(Login_number["Code"])
                d(resourceId="com.tencent.mobileqq:id/login",description=u"登录").click_exists(timeout=2)
                time.sleep(3)
                if check_login_stats(d) == 0:
                    print "登录成功"
                    login_stat = True
                    break
                else:
                    if d(resourceId="com.tencent.mobileqq:id/dialogText",description="帐号或密码错误，请重新输入。").exists:
                        d.make_toast("你输入的帐号或密码不正确，请重新输入。",5)
                        d(resourceId="com.tencent.mobileqq:id/dialogRightBtn", description="确定").click_exists(timeout=2)
                        # d(description=u"关闭").click_exists(timeout=2)
                        d(description="请输入QQ号码或手机或邮箱").clear_text()
                        d(description="请输入QQ号码或手机或邮箱").set_text(Login_number["QQ"])
                        d(resourceId="com.tencent.mobileqq:id/password").clear_text()
                        d(resourceId="com.tencent.mobileqq:id/password").set_text(Login_number["Code"])
                        d(resourceId="com.tencent.mobileqq:id/login",description=u"登 录").click_exists(timeout=2)
                        time.sleep(5)
                        if check_login_stats(d) == 0:
                            print "登录成功"
                            login_stat = 0
                            break

                        else:
                            print "请重新获取登录账号密码"

            if login_stat:
                d.make_toast("登录失败，请人为手动重新登录.", 5)
                d(resourceId="com.tencent.reading:id/btn_share", text="取消").click_exists(timeout=2)
                d(resourceId="com.tencent.reading:id/btn_back").click_exists(timeout=2)
            else:
                d = Read_News.backtohome(d)
                break
        else:
            print "请正确提供账号密码，及登录的账号类型"
    return d

def check_login_stats_withchar(d):
    d = Read_News.backtohome(d)
    if d(resourceId="com.tencent.reading:id/nav_tv", text=u"未登录").exists:
        register(d, Login_number)
    else:
        print("账号登录成功")


def send_code_for_qqlogin(d, codelist):
    k = 100
    for i in codelist:
        d(resourceId="ccom.tencent.mobileqq:id/name", text=u"请输入短信验证码").clear_text()
        d(resourceId="ccom.tencent.mobileqq:id/name", text=u"请输入短信验证码").set_text(i)
        d(resourceId="com.tencent.mobileqq:id/name", text=u"确定").click()
        time.sleep(3)

        # d(resourceId="com.tencent.reading:id/send_btn", text="获取验证码").click_exists(timeout=5)
        if d(resourceId="com.tencent.reading:id/mine_tab_better_header_user_name").exists:
            print("登录成功")
            k = 0
            break
        else:
            continue
    if k == 0:
        return 0
    else:
        return 1


def register_for_QQ(d, Login_number):
    time.sleep(1)
    d.press("home")
    time.sleep(2)
    d = Read_News.start_app_QQ(d, type_detect="login")
    time.sleep(1)
    if d(text=u"登 录").exists:
        d(text=u"登 录").click_exists(timeout=1)
    if d(
        resourceId="com.tencent.mobileqq:id/login",
        className="android.widget.Button",
            description="登录").exists:
        d(description="请输入QQ号码或手机或邮箱", text="QQ号/手机号/邮箱").clear_text()
        d(description="请输入QQ号码或手机或邮箱",
          text="QQ号/手机号/邮箱").set_text(Login_number["QQ"])
        d(resourceId="com.tencent.mobileqq:id/password").set_text(
            Login_number["Code"])
        d(description=u"登录").click_exists(timeout=2)
        login_stat = 1
        if d(resourceId="com.tencent.mobileqq:id/ug_btn").exists:
            d(resourceId="com.tencent.mobileqq:id/ug_btn").click()
            codelist = list(set(Get_SMSRec.check_codelist()))
            temp = "获得验证码 %s" % (str(codelist))
            d.make_toast(temp, 5)
            for resent_number in range(1, 2):
                login_stat = send_code_for_qqlogin(d, codelist)
                if login_stat == 1:
                    if d(
                        resourceId="com.tencent.mobileqq:id/name",
                            text=u"重新发送").exists():
                        d(resourceId="com.tencent.mobileqq:id/name",
                          text=u"重新发送").click_exists(timeout=60)
                        new_codelist = list(set(Get_SMSRec.check_codelist()))
                        codelist = list(
                            set(new_codelist).difference(
                                set(codelist)))
                elif login_stat == 0:
                    break

            if login_stat == 1:
                print("登录失败，请人为手动重新登录.")
                d(resourceId="com.tencent.mobileqq:id/ivTitleBtnLeft").click_exists(timeout=2)
                d(resourceId="com.tencent.mobileqq:id/ivTitleBtnRightText").click_exists(timeout=2)
        time.sleep(5)
    else:
        d.make_toast("登录界面有误", 3)

    d(resourceId="com.tencent.mobileqq:id/ivTitleBtnLeftButton").click_exists(timeout=3)  # 跳过皮肤装饰

    if check_qqlogin_stats(d) == 0:
        print("登录成功")
    else:
        print("请重新获取登录账号密码")
    return d


if __name__ == '__main__':
    #Login_number = {"Type":"Phone","Phone": "13267126886", "QQ":"532199541", "Code": "521liaoshengyou"}
    Login_number = {
        "Type": "QQ",
        "Phone": "13267126886",
        "QQ": "532199541",
        "Code": "521liaoshengyou"}
    d = u2.connect('http://0.0.0.0:7912')
    register(d, Login_number)
