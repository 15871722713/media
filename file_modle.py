#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JinHua
# @Date    : 2020-04-15 10:56:48
# @Contact : hgu_autotesta103@fiberhome.com
# @Site    :
# @File    : file_modle.py
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


def move(filename, path):
    print('move {} to {}{}'.format(filename, path, filename.split('\\')[-1]))
    os.popen('move {} {}{}'.format(filename, path, filename.split('\\')[-1]))


def main():
    dirname = 'Video\\TengXun\\'
    path = 'Video\\'
    allFile = glob.glob(dirname + '*.mp4')
    for filename in allFile:
        old_md5 = get_md5(filename)
        fileAppend(filename)
        new_md5 = get_md5(filename)
        print('filename is :{}\rold_md5 is :{}\rnew_md5 is :{}'.format(filename, old_md5, new_md5))
        move(filename, path)


if __name__ == '__main__':
    main()
