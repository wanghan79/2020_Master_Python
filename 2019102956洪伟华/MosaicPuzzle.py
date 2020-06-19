'''
    @Project: python 大作业
    @File   : MosaicPuzzle.py
    @Author : hong weihua
    @E-mail : hwh_cum@163.com
    @Date   : 2020-06-15
    @info   :
    -通过传入一张照片，利用现有的数据集，实现这张照片的蒙太奇照片
'''

import cv2
import numpy as np
import os
import collections

#图片准备阶段：数据集图片归一化
def resizeImage(imagePath,savePath):
    files=os.listdir(imagePath)
    #遍历所有图片文件，归一化
    for file in files:
        imgPath=imagePath+"//"+file
        img=cv2.imread(imgPath)
        img=cv2.resize(img, (100, 100))
        cv2.imwrite(savePath + "\\" + file, img)
    cv2.waitKey()
    return True

#图片准备阶段：数据集建立索引，保存每张图片出现次数最多的像素值然后保存到文件中
def createIndex(imagePath,txtPath):
    files=os.listdir(imagePath)
    txtFile=open(txtPath,'w')
    for file in files:
        li=[]
        txt=''
        imgPath=imagePath+"//"+file
        img=cv2.imread(imgPath)
        shape=np.shape(img)
        height=shape[0]
        width=shape[1]
        for i in range (height):
            for j in range(width):
                b = img[i, j, 0]
                g = img[i, j, 1]
                r = img[i, j, 2]
                li.append((b, g, r))
        #计算图片中像素值出现最多的颜色
        most = collections.Counter(li).most_common(1)
        txt+=file
        txt+=":"
        txt+= str(most[0][0]).replace("(","").replace(")","")
        txt+="\n"
        txtFile.write(txt)
    txtFile.close()

#开始制作马赛克 读取索引文件
def readIndex(txtPath):
    file=open(txtPath,"r")
    dic=[]
    #按行搜索
    for line in file.readlines():
        #按 : 分割字符 文件名+B,G,R
        temp=line.split(":")
        imgName=temp[0]
        bgr=temp[1].split(",")
        #转为0~255
        b=int(bgr[0])
        g=int(bgr[1])
        r=int(bgr[2])
        dic.append((imgName,(b,g,r)))
    return dic

if __name__ == '__main__':
    imagePath="D://pythonData//GrandsCausses2.jpg"
    txtPath="D://BaiduNetdiskDownload//index.txt"
    filepath=""
    saveImagePath="D://BaiduNetdiskDownload//resize"
    resultPath="D://pythonData//GrandsCaussesResult2.jpg"
    #resizeImage(imagePath,saveImagePath)
    #createIndex(saveImagePath,txtPath)
    image=cv2.imread(imagePath)
    shape=np.shape(image)
    height = shape[0]
    width = shape[1]
    result=np.zeros((100*height,100*width,3),dtype=np.uint8)
    list=readIndex(txtPath)
    for i in range(height):
        for j in range(width):
            b = image[i, j, 0]
            g = image[i, j, 1]
            r = image[i, j, 2]  # 获取图像当前位置的BGR值
            for item in list:
                imgb = item[1][0]
                imgg = item[1][1]
                imgr = item[1][2]  # 获取索引文件的RGB值
                distance = (imgb - b) ** 2 + (imgg - g) ** 2 + (imgr - r) ** 2  # 欧式距离
                if distance < 100:
                    filepath = saveImagePath + "\\" + str(item[0])  # 定位到具体的图片文件
                    break
            little = cv2.imread(filepath)  # 读取整个最相近的图片
            result[i * 100:(i + 1) * 100, j * 100:(j + 1) * 100] = little  # 把图片放到大图的相应位置

    cv2.imwrite(resultPath, result)  # 输出大图到文件中

