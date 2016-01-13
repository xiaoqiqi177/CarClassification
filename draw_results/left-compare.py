#!/usr/bin/env python

import matplotlib.pyplot as plt
import os, sys, cv2

if __name__ == '__main__':

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    input1 = open(file1, 'r')
    input2 = open(file2, 'r')
    input3 = open(file3, 'r')
    lines1 = input1.readlines()
    lines2 = input2.readlines()
    lines3 = input3.readlines()
    
    num = 0
    ll =[l for l in lines2 if l not in lines1] #not miss in fact

    results=[]
    for l in lines3:
        if l not in ll:
            results.append(l)
            num += 1
    import IPython
    IPython.embed()
