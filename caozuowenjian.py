# coding:utf-8

import win32ui
import winreg
import chardet
import file
import tkinter
import tkinter.messagebox  # 这个是消息框，对话框的关键
from bs4 import UnicodeDammit
from tkinter import StringVar, IntVar
from tkinter import *

filePath = ''

'''
获取当前电脑的桌面路径
'''


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    # winreg.QueryValueEx(key, "Desktop")[0] #返回的是Unicode类型数据
    Desktop_path = str(winreg.QueryValueEx(key, "Desktop")[0])  # Unicode转化为str
    return Desktop_path


'''
获取文件选择对话框选中的文件路径
返回值: 'c:/intimate.txt'
'''


def get_FileDialogPath():
    global filePath
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir(get_desktop())  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    filename = dlg.GetPathName()  # 获取选择的文件名称
    label1.config(text='当前操作文件:' + filename)
    label2.config(text='当前文件的编码格式:' + get_FileFormat(filename))
    filePath = filename


def get_FileEncoding(path):
    """
    查看文件的编码格式
    返回值:'ISO-8859-9'  'utf-8'   'GB2312'
    path     'c:/intimate.txt'
    """
    f = open(path, 'rb')
    data = f.read()
    FileEncode = chardet.detect(data)
    f.close()
    return FileEncode['encoding']


def get_FileFormat(path):
    """
    得到文件的编码格式
    返回值:'ISO-8859-9'  'utf-8'   'GB2312'
    path     'c:/intimate.txt'
    """
    f = open(path, 'rb')
    data = f.read()
    f.close()
    dammit = UnicodeDammit(data)
    f.close()
    return dammit.original_encoding


def form_Creat():
    """
    窗体创建
    """
    form = tkinter.Tk()
    form.title('Excel辅助')

    # 屏幕宽高
    form_w = 400
    form_h = 400

    # 居中
    ws = form.winfo_screenwidth()
    hs = form.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (form_w / 2)
    y = (hs / 2) - (form_h / 2)
    form.geometry('%dx%d+%d+%d' % (form_w, form_h, x, y))
    return form


def form_Close(form):
    form.destroy()


def count_sum(filePath):
    lines = file.readFileLinesDelkonghang(filePath)

    count = 0
    i = 0
    for item in lines:
        print(item)
        listbox.insert(i, item)  # 插入数据，
        count = count + int(item)
        i = i + 1
    print(count)
    listbox.pack()
    label3.config(text='当前文件每行累加值:' + str(count))
    label3.pack()


form = form_Creat()
global listbox
listbox = Listbox(form)
global label3
label3 = tkinter.Label(form, text='当前文件每行累加值:')

tkinter.Button(form, text='选择文件', command=get_FileDialogPath).pack()
label1 = tkinter.Label(form, text='当前操作文件:')
label1.pack()  # 显示窗口
label2 = tkinter.Label(form, text='当前文件的编码格式:')
label2.pack()  # 显示窗口

tkinter.Button(form, text='求和', command=lambda: count_sum(filePath)).pack()
tkinter.Label(form, text='文件内容:').pack()
form.mainloop()  # 显示窗口

