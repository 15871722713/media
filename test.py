#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JinHua
# @Date    : 2020-04-15 10:56:48
# @Contact : hgu_autotesta103@fiberhome.com
# @Site    :
# @File    : test.py
# @Software: PyCharm
# @Desc    :
# @license : Copyright(C), cienet


import os
import glob


def fileAppend(filename):
    myfile = open(filename, 'a')
    myfile.write("####&&&&%%%%")
    myfile.close


def get_md5(filename):
    files_md5 = os.popen('certutil -hashfile {} MD5'.format(filename)).read().strip().split('\n')

    return files_md5[1]


if __name__ == '__main__':
    filename = '你们知道我说了什么笑话吗.mp4'
    print(get_md5(filename))
    fileAppend(filename)
    print(get_md5(filename))
    # dirname = r'C:\Users\XXXX\Desktop\New folder'
    # allFile = glob.glob(dirname + os.sep + '*.mp4')

    # for filename in allFile:
    #     fileAppend(filename)
    #     print(filename + 'is Changed.')
