#!/usr/bin/env python

import matplotlib.pyplot as plt
import os, sys, cv2

if __name__ == '__main__':

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    input1 = open(file1, 'r')
    input2 = open(file2, 'r')
    input_all = open(file3, 'r')
    lines1 = input1.readlines()
    lines2 = input2.readlines()
    pics = input_all.readlines()
    pics = [p[:-1] for p in pics]
    new_lines1 = [l1.split()[0] for l1 in lines1 if float(l1.split()[1])>0.5]
    new_lines2 = [l2.split()[0] for l2 in lines2 if float(l2.split()[1])>0.5]
    left_lines1 = [name1+'\n' for name1 in pics if name1 not in new_lines1]
    left_lines2 = [name2+'\n' for name2 in pics if name2 not in new_lines2]
    
    output1 = open('left_1.txt','w')
    output1.writelines(left_lines1)
    output2 = open('left_2.txt','w')
    output2.writelines(left_lines2)
    
    import IPython
    IPython.embed()
