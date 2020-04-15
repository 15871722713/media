#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JinHua
# @Date    : 2020-04-14 16:50:49
# @Contact : hgu_autotesta103@fiberhome.com
# @Site    :
# @File    : get_video.py
# @Software: PyCharm
# @Desc    :
# @license : Copyright(C), cienet

import re
import os
import json
import time
import requests

from bs4 import BeautifulSoup

pattImg = re.compile("jpg|png|bmp")
nowPath = os.getcwd()
WeiBoUrl = "https://s.weibo.com/video?q=%E5%86%9B%E4%BA%8B&xsort=hot&hasvideo=1&tw=video"
#application/json; charset=utf-8
headersHtml = {'content-type': 'text/html; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
headersJson = {'content-type': 'application/json; charset=utf-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.get(WeiBoUrl, headers=headersHtml)
if os.path.exists(nowPath + "\\Video"):
    pass
else:
    os.mkdir("Video")


class videoSpider(object):
    # os.system('you-get.exe https://weibo.com/tv/v/H6qvCfQRe?fid=1034:4315318475025961 -o '+os.getcwd()+"\\Video")
    # 新浪视频
    # http://so.video.sina.com.cn/s?wd=明星
    # 腾讯 最新filter
    # https://v.qq.com/x/search/?q=明星&filter=sort%3D1%26&cur=1
    # 爱奇艺
    # http://so.iqiyi.com/so/q_吴亦凡
    # 优酷
    # https://so.youku.com/search_video/q_吴亦凡
    # b站
    # https://search.bilibili.com/all?keyword=吴亦凡&order=stow

    def __init__(self):
        super(videoSpider, self).__init__()

    def GetXinLangVideoUrls(self, keyword):
        r = requests.get("http://so.video.sina.com.cn/interface/s?from=video&wd=" + keyword +
                         "&s_id=w00001&p=1&n=20&_=1544340510669", headers=headersJson)
        print(r.text)
        res = json.loads(r.text)  # 字符串转成dic，顺带转码
        XinLangPath = nowPath + "\\Video\\XinLang"
        connect = connectMysql()
        cursor = connect.cursor()
        try:
            os.mkdir(XinLangPath)
        except:
            pass
        for oneItem in res["list"]:
            url = oneItem["url"]
            thumburl = oneItem["thumburl"]
            videoname = oneItem["videoname"]
            videoinfo = oneItem["videoinfo"]
            videoname = videoname.replace("<span style=\"color:#C03\">", "")
            videoname = videoname.replace("</span>", "")
            videoinfo = videoinfo.replace("<span style=\"color:#C03\">", "")
            videoinfo = videoinfo.replace("</span>", "")
            os.system("you-get.exe " + url + " -o " + XinLangPath + " -O " + videoname)
            videoPath = XinLangPath + "\\" + videoname + ".flv"
            try:
                imgType = pattImg.findall(thumburl)[0]
            except:
                continue
            r = requests.get(thumburl)
            imgPath = XinLangPath + '\\' + videoname + "." + imgType
            print(imgPath)
            with open(imgPath, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            videoPath = videoPath.replace("\\", "$$$")
            imgPath = imgPath.replace("\\", "$")
            print(videoname, videoinfo, videoPath, imgPath)
            print(type(videoname), type(videoinfo), type(videoPath), type(imgPath))

    def GetTengXunVideoUrls(self, keyword):
        i = 1
        while i < 40:
            r = requests.get("https://v.qq.com/x/search/?q=" + keyword +
                             "&filter=sort%3D1%26&cur=" + str(i), headers=headersJson)
            i += 1
            soup = BeautifulSoup(r.text)
            divs = soup.find_all("div", class_="result_item result_item_h _quickopen")
            TengXunPath = nowPath + "\\Video\\TengXun"

            try:
                os.mkdir(TengXunPath)
            except:
                pass
            for div in divs:
                aVideo = div.find_all("a", class_="figure result_figure")
                aImg = div.find_all("img")
                videoUrl = aVideo[0].get("href")
                thumbUrl = "http:" + aImg[0].get("src")
                videoName = aImg[0].get("alt")
                videoName = videoName.replace("\x05", "")
                videoName = videoName.replace("\x06", "")
                videoInfo = ""
                try:
                    imgType = pattImg.findall(thumbUrl)[0]
                except:
                    imgType = "jpg"
                videoType = "mp4"
                imgPath = TengXunPath + '\\' + videoName + "." + imgType
                print(imgPath)
                r = requests.get(thumbUrl)
                with open(imgPath, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
                os.system("you-get.exe " + videoUrl + " -o " + TengXunPath + " -O " + videoName)
                TengXunPathSql = TengXunPath.replace("\\", "$$")
            time.sleep(5)


videoSpider().GetTengXunVideoUrls('笑话')
# videoSpider().GetXinLangVideoUrls('搞笑')
