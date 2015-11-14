#!/usr/bin/env python

import matplotlib.pyplot as plt
import os, sys, cv2


if __name__ == '__main__':
   
    points_file = sys.argv[1]
    print points_file
    p1 = points_file.rfind("_")
    p2 = points_file.index(".")
    kind = points_file[p1+1:p2]
    print kind
    fin = open(points_file, "r")
    alllines = fin.readlines()
    fin.close()

    fout = open("./result_record/record.txt","a");
    for eachline in alllines:
        arr = eachline.split()
        pic_file = arr[0]
        weight = float(arr[1])
        if weight < 0.5:
            continue
        temp = pic_file
        im_file = pic_file+".jpg"
        im = cv2.imread("../test_pic/"+im_file)
        a = float(arr[2])
        b = float(arr[3])
        c = float(arr[4])
        d = float(arr[5])
        crop_img = im[b:d, a:c]
        cv2.imwrite("./result_pic/"+kind+"_"+str(weight)+".jpg",crop_img);
        fout.write(kind+"_"+str(weight)+" "+pic_file+" "+kind+" "+str(weight)+"\n");
   
    fout.close()
