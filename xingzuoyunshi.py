# -*- coding: UTF-8 -*-
__author__ = 'Chiachyi'
__time__ = '2017年11月5日 21:45:53'
__idea__ = '更新更多内容'
__future__ = '各星座运势都齐了'

import urllib
from bs4 import BeautifulSoup

def getdom(url):
    resps = urllib.request.urlopen(url)
    html = resps.read()
    data = html.decode('utf-8')
    soup = BeautifulSoup(data,'html5lib')
    #print(soup.body.p)

    for list in soup.body.p:
        if list.string==None:
            continue
        else:
            print(list.string)
    return

def yunshi():
    print("请选择您的星座！")
    print('1.水瓶座')
    print('2.白羊座')
    print('3.金牛座')
    print('4.双子座')
    print('5.巨蟹座')
    print('6.狮子座')
    print('7.处女座')
    print('8.天秤座')
    print('9.天蝎座')
    print('10.射手座')
    print('11.摩羯座')
    xz = input("请输入星座所对应的数字:")
    if xz.isdigit():
        xz = int(xz)
        dic =['aquarius','aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn'] 
        url = "http://www.xzw.com/fortune/"+dic[xz-1]+"/"
        getdom(url)
    else:
        print("输入错误！")
    return


