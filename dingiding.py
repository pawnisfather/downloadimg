#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: xxxxxxxx
import requests
import json
import sys
import os


headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=286015484db95362e91f950f482bfe67fa537c1d459c087d9fd366c97761c4d2"


def msg(test):

    json_text = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                "18186984250"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }

    }
    print(requests.post(api_url, json.dumps(json_text), headers=headers).content)

# def msg(text):
#     json_text= {
#      "msgtype": "text",
#         "at": {
#             "atMobiles": [
#                 "xxxxxxxxxx"写被@人的电话
#             ],
#             "isAtAll": False
#         },
#         "text": {
#             "content": text
#         }
#     }
#     print(requests.post(api_url,json.dumps(json_text),headers=headers).content)


if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
