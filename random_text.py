#! /usr/bin/python

import os
import random
f = open('train.txt', 'r')
fout = open('out.txt','a')
mm = f.readlines()
random.shuffle(mm)
for i in mm:
    fout.write(i)

