#!/usr/bin/env python
'''
===============================================================================
Image Segmentation using GrabCut algorithm.
This sample shows image segmentation using grabcut algorithm.
USAGE:
    python grabcut.py <filename>

===============================================================================
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import datetime

import sys

class App():
    BLUE = [255,0,0]        # rectangle color

    # setting up flags
    rect = (0,0,1,1)
    drawing = False         # flag for drawing curves
    rectangle = False       # flag for drawing rect
    rect_over = False       # flag to check if rect drawn
    rect_or_mask = 100      # flag for selecting rect or mask mode
    thickness = 3           # brush thickness

    def run(self):
        # Loading images
        if len(sys.argv) == 2:
            filename = sys.argv[1] # for drawing purposes
        else:
            print("No input image given, so loading default image, lena.jpg \n")
            print("Correct Usage: python grabcut.py <filename> \n")
            filename = 'lena.jpg'


        imgpath = "D:/software-place/AIvision-resistance/testpictures/OB.jpg"
        begin = datetime.datetime.now()
        print(imgpath)
        self.img = cv.imread(imgpath)
        self.img2 = self.img.copy()                               # a copy of original image
        self.mask = np.zeros(self.img.shape[:2], dtype = np.uint8) # mask initialized to PR_BG
        self.output = np.zeros(self.img.shape, np.uint8)           # output image to be shown

        rows, columns, channels = self.img.shape
        self.rect = ( (int)(columns/3),(int)(rows/3), (int)(columns-columns/3-columns/3), (int)(rows-rows/3-rows/3))
        cv.rectangle(self.img, ((int)(columns/3), (int)(rows/3)), ((int)(columns-columns/3), (int)(rows-rows/3),), self.BLUE, 16)
        self.rect_or_mask = 0
        for num in range(0, 5):
            try:
                bgdmodel = np.zeros((1, 65), np.float64)
                fgdmodel = np.zeros((1, 65), np.float64)
                if (self.rect_or_mask == 0):  # grabcut with rect
                    cv.grabCut(self.img2, self.mask, self.rect, bgdmodel, fgdmodel, 1, cv.GC_INIT_WITH_RECT)
                    temp = np.where((self.mask == 1) + (self.mask == 3), 255, 0).astype('uint8')
                    cv.imwrite("temp_b" + str(num) + ".jpg", temp)
                    self.rect_or_mask = 1
                elif (self.rect_or_mask == 1):  # grabcut with mask
                    cv.grabCut(self.img2, self.mask, self.rect, bgdmodel, fgdmodel, 1, cv.GC_INIT_WITH_MASK)
                    temp = np.where((self.mask == 1) + (self.mask == 3), 255, 0).astype('uint8')
                    cv.imwrite("temp_b" + str(num) + ".jpg", temp)
            except:
                import traceback
                traceback.print_exc()
        mask2 = np.where((self.mask == 1) + (self.mask == 3), 255, 0).astype('uint8')
        self.output = cv.bitwise_and(self.img2, self.img2, mask=mask2)
        end = datetime.datetime.now()
        k = end - begin
        print("时间差： " + str(k.total_seconds()))
        inputname = "input_b.jpg"
        outputname = "output_b.jpg"
        cv.imwrite(inputname, self.img)
        cv.imwrite(outputname, self.output)


if __name__ == '__main__':
    print(__doc__)
    App().run()
    cv.destroyAllWindows()