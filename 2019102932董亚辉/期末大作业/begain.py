#!/usr/bin/python3
# Introduction: Introduce you file
from tkinter.filedialog import  askdirectory
# 导入创建的工具类
from annotation import SimpleBBoxLabeling

if __name__ == '__main__':
    dir_with_images = askdirectory(title='choose images path?')
    labeling_task = SimpleBBoxLabeling(dir_with_images)
    labeling_task.start()
