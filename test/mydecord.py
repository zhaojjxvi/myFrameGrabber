# import os
import decord
from datetime import datetime
from PIL import Image

# 视频文件路径
video_path = r'../media/1.mp4'


def frame_grabber(path):
    # 创建VideoReader对象
    video = decord.VideoReader(path)

    # 逐帧读取视频并导出为图片
    frame_count = 0
    for frame in video:
        frame_count += 1
        frame_name = f'frame_{frame_count}.jpg'
        img = Image.fromarray(frame.asnumpy())  # 将帧转换为PIL Image对象
        # print(frame_count, end='')
        # img.save(frame_name)  # 将PIL Image保存为图片
    print('')


if __name__ == '__main__':
    # Calling the function
    print(datetime.now())
    frame_grabber(r"../media/1.mp4")
    print(datetime.now())
    frame_grabber(r"../media/2.mp4")
    print(datetime.now())
    frame_grabber(r"../media/3.mp4")
    print(datetime.now())
