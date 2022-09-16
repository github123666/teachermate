import os
import requests
import time
import re

openid = input("请输入openid,或带有openid的链接:")
if len(openid) > 32:
    openid = re.findall("openid=(.{0,32})", openid)
    print(openid)
print("开始运行")
while len(openid[0]) == 32:
    headers = {'Host': 'v18.teachermate.cn', 'Accept': '*/*', 'openId': "9a3feda255ad93032b24d4a2be2c3c89",
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'content-type': 'application/json',
               'Origin': 'https://v18.teachermate.cn',
               'user-agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; SM-G977N Build/LMY48Z) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
               'Connection': 'keep-alive'}
    time.sleep(10)
    rsp = requests.get(
        url="https://v18.teachermate.cn/wechat-api/v1/class-attendance/student/active_signs", headers=headers).json()
    if type(rsp) == dict:
        print("openid already failed")
    elif not rsp:
        print("clock_in no start ")
    else:
        if rsp[0]["isGPS"] or rsp[0]["isQR"]:
            print("请手动签到")
            time.sleep(500)
        else:
            print("执行签到")
            os.system(
                "start https://v18.teachermate.cn/wechat-pro-ssr/student/sign?openid=b8e0ca125c0538a1bf5522c26a7de700")
            time.sleep(500)
