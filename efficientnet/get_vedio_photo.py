# -------------------------------------------------
# @Time    : 2020/6/23 22:08
# @Author  : RunRun
# @File    : test
# @Software: PyCharm
#
# -------------------------------------------------
# 功能
#
#   截取视频帧
#
#
# 结果
#
#
#
import cv2,os
save_path=r"D:"      #存储的位置
path = r"D:\Desktop\MP4"    #要截取视频的文件夹

filelist = os.listdir(path)     #读取文件夹下的所有文件
print(filelist)
for item in filelist:
    if item.endswith('.mp4'):     #根据自己的视频文件后缀来写，我的视频文件是mp4格式
        print(item)
        try:
            src = os.path.join(path, item)
            vid_cap = cv2.VideoCapture(src)    #传入视频的路径
            success, image = vid_cap.read()
            count = 0
            while success:
                vid_cap.set(cv2.CAP_PROP_POS_MSEC, 0.5 * 1000 * count)   #截取图片的方法  此处是0.5秒截取一个  可以改变参数设置截取间隔的时间
                video_to_picture_path= os.path.join(save_path, item.split(".")[0])    #视频文件夹的命名
                if not os.path.exists(video_to_picture_path):   #创建每一个视频存储图片对应的文件夹
                    os.makedirs(video_to_picture_path)
                cv2.imwrite(video_to_picture_path+"/" + str(count) + ".jpg",
                            image)       #存储图片的地址 以及对图片的命名
                success, image = vid_cap.read()
                count += 1
            print('Total frames: ', count)     #打印截取的图片数目
        except:
            print("error")


