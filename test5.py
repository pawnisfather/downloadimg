import os
import urllib
import urllib.request
import ssl
import sys


ssl._create_default_https_context = ssl._create_unverified_context
def img_download(img_urls):  # 文件下载保存
    if img_urls is None or len(img_urls) == 0:
        print
        'no img can download'
        return

    cur_path = os.path.abspath(os.curdir)  # 获取当前绝对路径

    goal_path = cur_path + '/' + 'imgs'  # 想将文件保存的路径
    if not os.path.exists(goal_path):  # os.path.isfile('test.txt') 判断文件夹/文件是否存在
        os.mkdir(goal_path)  # 创建文件夹
    count = 1  # 用于给图片命名
    for img in img_urls:
        print(img)


        urllib.request.urlretrieve(img, goal_path + '/' + str(count) + '.jpg')
        count = count + 1

if __name__ == '__main__':


    apitextlocations = sys.argv[1]  # 页面地址
    # printrint(len(open(apitextlocations).readlines()))

    img_download(open(apitextlocations).readlines())
