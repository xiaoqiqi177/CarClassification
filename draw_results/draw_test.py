#!/usr/bin/env python

import matplotlib.pyplot as plt
import os, sys, cv2

if __name__ == '__main__':

    points_file = sys.argv[1]
    print points_file
    p1 = points_file.rfind("_")
    p2 = points_file.rfind(".")
    kind = points_file[p1+1:p2]
    print kind
    fin = open(points_file, "r")
    alllines = fin.readlines()
    fin.close()
    temp = 0
    for eachline in alllines:
        arr = eachline.split()
        pic_file = arr[0]
        weight = float(arr[1])
        if weight < 0.5:
            continue
        temp = pic_file
        im_file = pic_file+".jpg"
       
        img = cv2.imread("../test_pic/"+im_file)     
        a = int(float(arr[2]))
        b = int(float(arr[3]))
        c = int(float(arr[4]))
        d = int(float(arr[5]))
        cv2.namedWindow("Image")
        cv2.rectangle(img,(a,b),(c,d),(0,255,255),1)
        cv2.putText(img, str(kind)+':'+str(weight), (a,b-2), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255))   
        cv2.imwrite("pic_annotated/"+pic_file+'.jpg', img)
      
        cv2.destroyAllWindows()
