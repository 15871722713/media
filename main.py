#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JinHua
# @Date    : 2020-04-14 16:50:13
# @Contact : hgu_autotesta103@fiberhome.com
# @Site    :
# @File    : main.py
# @Software: PyCharm
# @Desc    :
# @license : Copyright(C), cienet

from file_modle import main
from get_video import videoSpider


videoSpider().GetTengXunVideoUrls('笑话', 2)
main()
