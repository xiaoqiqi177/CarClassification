#!/usr/bin/python
import sys
import os
import numpy as np
import shutil

typee = sys.argv[1]
image_path = '/home/qqxiao/Desktop/final_pics_without_anno/'+typee+'/'
images = [x for x in os.listdir(os.path.dirname(image_path))]
num = len(images)
axis = [int(num/50)*i for i in range(50)]
for i in range(num):
    if i in axis:
        shutil.copy(image_path+images[i],'/home/dataset/dataset_faster_rcnn/'+typee+'/train/')
    else:
        shutil.copy(image_path+images[i],'/home/dataset/dataset_faster_rcnn/'+typee+'/test/')

#import IPython
#IPython.embed()
