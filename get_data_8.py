#!/usr/bin/python
import sys
import os
import numpy as np
import shutil
import random

source_dir='/home/dataset/cropped_imgs/images_from_testset/'
dest_dir='/home/qqxiao/Desktop/caffe/data/vgg_back_8/'
cars=['a6l','accord','buick','byd','corolla','cruze','faw','satana']

f_train = open(dest_dir+'train.txt','a')
f_test = open(dest_dir+'test.txt','a')
f_val = open(dest_dir+'val.txt','a')
train_lines = []
test_lines = []
val_lines = []
train_images = []
test_images = []

for i in range(len(cars)):
    car = cars[i]
    image_path = source_dir+car+'/back/'
    images = [x for x in os.listdir(os.path.dirname(image_path))]
    num = len(images)
    for j in range(int(num*0.8)):
        image=images[j]
        train_images.append(image_path+image)
        train_lines.append(image+' '+str(i)+'\n')
    for j in range(int(num*0.8), num):
        image=images[j]
        test_images.append(image_path+image)
        val_lines.append(image+' '+str(i)+'\n')
        test_lines.append(image+' 0'+'\n')

train_items=zip(train_images, train_lines)
random.shuffle(train_items)
for image, line in train_items:
    shutil.copy(image, dest_dir+'train/')
    f_train.write(line)
test_items=zip(test_images, test_lines, val_lines)
random.shuffle(test_items)
for image, test_line, val_line in test_items:
    shutil.copy(image, dest_dir+'val/')
    f_test.write(test_line)
    f_val.write(val_line)

f_train.close()
f_test.close()
f_val.close()
