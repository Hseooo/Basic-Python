# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:31:57 2022

@author: USER
"""

score = int(input("성적을 입력하시오"))
if score >= 90 :
    print("학점 A")
elif score >= 70 :
    print("학점 B")
elif score >= 40 :
    print("학점 C")
else :
    print("학점 D")