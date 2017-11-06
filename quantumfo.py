# -*- coding: UTF-8 -*-
__author__ = 'Chiachyi'
__time__ = '2017年11月5日 17:51:41'
__idea__ = '之后利用一部分nlp的知识和爬虫的知识写运势'
__future__ = '用量子碰撞实现随机数'

from xingzuoyunshi import yunshi
from bagua import qigua
from lingqian import chouqian,wenshi
from clients import talkfo

def liangzifoxue():
    print('')
    print('')
    print('')
    print('')
    print('========================================')
    print('===========量子佛学欢迎你===============');
    print('=========Welcome to Quantumfo===========');
    print('===============1.抽签===================')
    print('===============2.问事===================')
    print('===============3.运势===================')
    print('===============4.八字===================')
    print('===============5.易经===================')
    print('===============6.交流===================')
    print('===============7.作者===================')
    a = input("---------------请选择-------------------");
    print('')
    print('')
    print('')
    if a == '1':
        print('         ===请等待几秒钟===')
        chouqian()        
    elif a == '2':
        print('         ===请等待几秒钟===')
        wenshi()
    elif a == '3':
        yunshi()
    elif a == '4':
        qigua()
    elif a == '5':
        print('在开发')
    elif a == '6':
        talkfo()
    elif a == '7':
        print("相信概率，敬畏神灵(￣3￣)！")
    else:
        print("输入错误")  
    print("--------爱笑的汉子运气最好了------------")
    return




while 1:
    liangzifoxue()
