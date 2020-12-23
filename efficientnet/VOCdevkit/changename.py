# -------------------------------------------------
# @Time    : 2020/6/10 15:59
# @Author  : RunRun
# @File    : changename
# @Software: PyCharm
#
# -------------------------------------------------
# 功能
#
#  遍历文件夹下的所有文件并重命名
#
import os


def rename():


    path = r"E:\Desktop\动物识别检测\efficientnet\animals\dog"    # 文件路径
    filelist = os.listdir(path)                     # 该文件夹下的所有文件
    count = 0

    for file in filelist: # 遍历所有文件 包括文件夹
        Olddir = os.path.join(path,file)  # 原来文件夹的路径
        if os.path.isdir(Olddir):    # 如果是文件夹，则跳过
            continue
        filename = os.path.splitext(file)[0]  # 文件名
        filetype = ".jpg"    # os.path.splitext(file)[1]   文件扩展名
        Newdir = os.path.join(path ,"dog_"+str(count)+filetype) #  引号内 改命名 count是计数
        os.rename(Olddir , Newdir)   # 重命名
        count += 1
    print("已完成重命名")


rename()