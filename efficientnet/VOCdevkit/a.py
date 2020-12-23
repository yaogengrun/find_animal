# -------------------------------------------------
# @Time    : 2020/6/22 14:50
# @Author  : RunRun
# @File    : a
# @Software: PyCharm
#
# -------------------------------------------------
# 功能
#
#   将所有数据的名字提取到txt文本
#
#
# 结果
#
#
#
#
#
import os
import random


xmlfilepath = 'Annotations'
xmlfilepath=r'D:\Desktop\yolo3-keras-master\VOC2012\Annotations'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
fallname = open(os.path.join('D:/Desktop/yolo3-keras-master/allname1.txt'), 'w')
for i in list:
    name = total_xml[i][:-4]+('\n')
    # print(name)
    fallname.write(name)

fallname.close()
