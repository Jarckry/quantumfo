# -*- coding: UTF-8 -*-
__author__ = 'Chiachyi'
__time__ = '2017年11月5日 17:51:41'
__idea__ = ''
__future__ = ''

import random
from time import sleep
def chou():
    sleep(3)
    c = int(int(random.random()*1000)/10);
    return c;

    
def chouqian():
    b = chou()
    print('         第',b,'号是你的签')
    if b <= 22:
        print("               上签")

    if b >= 22 & b<= 82 :
        print("               中签")

    else:
        print("               下签")
    return

def wenshi():
    c = chou()
    if c >= 82:
        print('                可行')
    elif c<=22 & c>= 82 :
        print('               不置可否')
    else:
        print('                不可行')


