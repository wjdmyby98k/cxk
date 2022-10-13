import os
import cv2

root = r'./images'  # 图片存放路径
height = 852  # 图片的宽
width = 480  # 图片的长度
fps = 25  # 设置想要写成的视频的帧率
fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
video = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc(*'MJPG'), fps, (height, width))  # 设置保存路径，创建视频流对象-格式一 ，帧率，长宽

file_list = os.listdir(root)
file_list.sort(key=lambda x: int(x[:-4]))
for item in file_list:
    print(item)
    if item.endswith('.jpg'):
        print(item)
        img = cv2.imread(os.path.join(root, item))  # 读取
        video.write(img)  # 合成视频
video.release()  # 释放
cv2.destroyAllWindows()
