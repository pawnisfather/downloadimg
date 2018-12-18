#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xlrd
import sys
import requests
import json
import os
import urllib
import urllib.request
import ssl
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from tkinter.filedialog import askdirectory


filename = "文件位置"
window = tk.Tk()
window.title('图片导出小工具')
window.geometry('400x100')
v = tk.StringVar()
v.set("文件位置")
path = tk.StringVar()

frame_root = tk.Frame(window)
frame_1 = tk.Frame(frame_root)
frame_2 = tk.Frame(frame_root)
frame_3 = tk.Frame(frame_root)



class Kk:
    filename=""
    targetdirname = ""

    def getColumnIndex(self,table, columnName):
        columnIndex = None
        #print table
        for i in range(table.ncols):
            #print columnName
            #print table.cell_value(0, i)
            if(table.cell_value(0, i) == columnName):
                columnIndex = i
                break
        return columnIndex

    def selectPath(self):
        path_ = askdirectory(initialdir=os.path.abspath(os.curdir))
        path.set(path_)
        self.targetdirname=path_


    def getFileName(self):

        filename = tkinter.filedialog.askopenfilename(filetypes=[("xls格式", "xls"), ("xlsx格式", "xlsx")],
                                                      initialdir=os.path.abspath(os.curdir))
        if filename is None:
            messagebox.askokcancel(message="请选择保存订单号的xlsx文件")

        print(filename)
        v.set(filename)
        self.filename=filename


        return filename

    def readExcelDataByName(self,fileName, sheetName):
        #print fileName
        table = None
        errorMsg = ""
        try:
            data = xlrd.open_workbook(fileName)
            table = data.sheet_by_name(sheetName)
        except Exception as msg:
            errorMsg = msg
        return table, errorMsg


    def readExcelDataByName(self,fileName, sheetName):
        #print fileName
        table = None
        errorMsg = ""
        try:
            data = xlrd.open_workbook(fileName)
            table = data.sheet_by_name(sheetName)
        except Exception as msg:
            errorMsg = msg
        return table, errorMsg

    def getordername(self):

        xlsfile= self.filename
        table = self.readExcelDataByName(xlsfile, 'Sheet1')[0]
        s=[]
        i = 1
        if table is None:
            return s
        else:
            while (i < table.nrows):

                testcase_id = table.cell_value(i, self.getColumnIndex(table, "救援号"))
                s.append(testcase_id)
                i+=1
            return s


    ssl._create_default_https_context = ssl._create_unverified_context

    def img_download(self,company,chepaihao):  # 文件下载保存
        # apitextlocations = sys.argv[1]  # 页面地址
        #
        # img_urls = open(apitextlocations).readlines()
        img_urls=self.getordername()
        if img_urls is None or len(img_urls) == 0:
            messagebox.askokcancel(message="当前选择表格文件为空，请重新选择保存订单号的表格文件")
            print("no img can download")
            return

        cur_path = os.path.abspath(os.curdir)  # 获取当前绝对路径

        # goal_path = cur_path + '/' + company +'/' + chepaihao  # 想将文件保存的路径
        if self.targetdirname is "":
            messagebox.askokcancel(message="目标文件夹未选择，将会保存在当前程序目录")
            self.targetdirname = cur_path


        goal_path=os.path.join( self.targetdirname,company, chepaihao)
        print(goal_path)
        if not os.path.exists(goal_path):  # os.path.isfile('test.txt') 判断文件夹/文件是否存在
            os.makedirs(goal_path)  # 创建文件夹
        count = 1  # 用于给图片命名
        imgname=chepaihao
        for img in img_urls:
            print(img)
            strcount=str(count)
            imgnames=imgname+strcount


            urllib.request.urlretrieve(img, goal_path + '/' + imgnames + '.jpg')
            count = count + 1

        print("完成")
        messagebox.askokcancel(message="执行完成")



            # apitextlocations = sys.argv[1]  # 页面地址
            # printrint(len(open(apitextlocations).readlines()))

            # img_download(open(apitextlocations).readlines())

    def downimg(self):
        api_url = "http://apitest.ely.work/api/user/user/login"
        for a in self.getordername():
            print(a)
            data = {'requestid': a}
            print(data)
            r = requests.post(url=api_url, data=data)
            print(r.json())
            s = json.loads(r.json())

        # datas = json.dumps({'account': 'caogu', 'password': 'caogu'})
        # date2= {'account': 'caogu', 'password': 'caogu'}
        # print(datas)
        # data2 = {'account': 'caogu', 'password': "caogu"}
        # data3 = {"data":{"account":"caogu", "password":"caogu"}}
        # r = requests.post(url=github_url, data=data2, json=datas)
        # # requests.post(url, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        #
        # print(r.text)
        # s= json.loads(r.text)
        # print(s.keys())



if __name__ == '__main__':
    kk=Kk()
    # filename = "文件位置"
    # window = tk.Tk()
    # window.title('my window')
    # window.geometry('300x100')
    # v = tk.StringVar()
    # v.set("文件位置")

    w3 = tk.Label(frame_1, text="文件位置:")
    w4=tk.Entry(frame_1, textvariable=v)
    w3.pack(side="left")
    w4.pack(side="left")
    w = tk.Button(frame_1, text="获取文件", command=kk.getFileName)
    print(v)

    w.pack(side="left")
    tk.Label(frame_2, text="目标路径:").pack(side="left")
    tk.Entry(frame_2, textvariable=path).pack(side="left")
    tk.Button(frame_2, text="路径选择", command=kk.selectPath).pack(side="left")
    w2 = tk.Button(frame_3, text="开始执行", command=lambda: kk.img_download("aaa", "bbb"))
    w2.pack()
    frame_1.pack()
    frame_2.pack()
    frame_3.pack()
    frame_root.pack()
    window.mainloop()


    # img_download("sss","aaa")
