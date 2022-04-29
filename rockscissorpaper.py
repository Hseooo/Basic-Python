# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:46:33 2022

@author: USER
"""

import random

def game():  # -1 0 1
    a=input("가위 바위 보! : ")
    b=random.randrange(0,3) # 0: 가위 1: 바위 2:보
    if a=='가위':
        a=0
        if b==0:
            print("비겼습니다")
        elif b==1:
            print("졌습니다")
        elif b==2:
            print("이겼습니다")
    elif a=='바위':
        a=1
        if b==0:
            print("이겼습니다")
        elif b==1:
            print("비겼습니다")
        elif b==2:
            print("졌습니다")
    elif a=='보':
        a=2
        if b==0:
            print("졌습니다")
        elif b==1:
            print("이겼습니다")
        elif b==2:
            print("비겼습니다")

game()