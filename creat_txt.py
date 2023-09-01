# -*- coding: utf8 -*-
import os
import random
xmlfilepath = r'/home/yolov7-yiwu/data/images/train'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
print(num)
list = range(num)
#test = open(r'/home/yolov7-yiwu/data/ImageSets/main/text.txt', 'w')
train = open(r'/home/yolov7-yiwu/data/ImageSets/main/train.txt', 'w')
#val = open(r'/home/yolov7-yiwu/data/ImageSets/main/val.txt', 'w')
k = 1
for i in list:
    name = r'/home/yolov7-yiwu/data/images/train' + '/' + total_xml[i] + '\n'
    print(k,name)
    train.write(name)
    k += 1

train.close()
#test.close()
#val.close()
