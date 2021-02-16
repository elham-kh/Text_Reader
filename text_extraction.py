# importing modules
import cv2
import pytesseract
from pytesseract import Output
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# reading image using opencv
image = cv2.imread('output.png')

cImage = np.copy(image) #image to draw lines
#converting image into gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# converting it to binary image by Thresholding
# this step is required if you have colored image because if you skip this part 
# then tesseract won't able to detect text correctly and this will give incorrect result
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# display image
cv2.imshow('threshold image', threshold_img)
# Maintain output window until user presses a key
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyWindow("gray")
canny = cv2.Canny(gray, 50, 150)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyWindow("canny")

# cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]) → lines
rho = 1
theta = np.pi/180
threshold = 50
minLinLength = 350
maxLineGap = 6
linesP = cv2.HoughLinesP(canny, rho , theta, threshold, None, minLinLength, maxLineGap)


def is_vertical(line):
    return line[0]==line[2]
    
def is_horizontal(line):
    return line[1]==line[3]


horizontal_lines = []


vertical_lines = []
    
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]        
        if (is_vertical(l)):
            vertical_lines.append(l)
                
        elif (is_horizontal(l)):
            horizontal_lines.append(l)

for i, line in enumerate(horizontal_lines):
    cv2.line(cImage, (line[0], line[1]), (line[2], line[3]), (0,255,0), 3, cv2.LINE_AA)
                      
for i, line in enumerate(vertical_lines):
    cv2.line(cImage, (line[0], line[1]), (line[2], line[3]), (0,0,255), 3, cv2.LINE_AA)
            
cv2.imshow("with_line", cImage)
cv2.waitKey(0)
cv2.destroyWindow("with_line") #close the window

#configuring parameters for tesseract
custom_config = r'--oem 3 --psm 6'
# now feeding image to tesseract
details = pytesseract.image_to_data(threshold_img, output_type=Output.DICT, config=custom_config, lang='eng')
print(details.keys())

total_boxes = len(details['text'])
for sequence_number in range(total_boxes):
    if int(details['conf'][sequence_number]) >30:
        (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
        threshold_img = cv2.rectangle(threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# display image
cv2.imshow('captured text', threshold_img)
# Maintain output window until user presses a key
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()