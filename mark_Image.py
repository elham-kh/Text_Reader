import cv2
from PIL import Image
import os
from matplotlib import pyplot
import numpy as np

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))


    
im = cv2.imread('page2.png')

imgSize = np.shape(im)

# Adaptive Thresholding requires the blocksize to be odd and bigger than 1
blockSize = 1 / 8 * imgSize[0] / 2 * 2 + 1
if blockSize <= 1:
    blockSize = imgSize[0] / 2 * 2 + 1
const = 10

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,blockSize = 23, C = const)

cv2.imwrite("thresh.png", thresh)


# Dilate to combine adjacent text contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
dilate = cv2.dilate(thresh, kernel, iterations=4)

# Find contours, highlight text areas, and extract ROIs
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

line_items_coordinates = []
for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)

    if y >= 600 and x <= 1000:
        if area > 10000:
            image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
            line_items_coordinates.append([(x,y), (2200, y+h)])

    if y >= 2400 and x<= 2000:
        image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
        line_items_coordinates.append([(x,y), (2200, y+h)])


pyplot.imshow(image)
pyplot.show()

