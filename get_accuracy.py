#!/usr/bin/python
import sys
import os
import numpy as np
import re

cars = ['a6l', 'accord', 'corolla', 'byd', 'satana', 'faw', 'buick', 'cruze']

fin = open('result2000.txt','r')
lines = fin.readlines()
right_num = 0
for i in range(len(lines)//6):
    truecar=''
    for car in cars:
        if car in lines[i*6]:
            truecar = car
            break
    if truecar.upper() in lines[i*6+1]:
        right_num += 1
        print right_num

print right_num
total_test = len(lines)//6
print total_test
print float(right_num*1.0/total_test)
fin.close()

