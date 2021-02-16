
# Import required packages 
import cv2 
import pytesseract 
import os
import matplotlib.pyplot as plt
  
# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
  
# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read image from which text needs to be extracted 
img = cv2.imread("page2.png") 
  
# Preprocessing the image starts 
  
# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

cv2.imshow("gray", img)
cv2.waitKey(0)
cv2.destroyWindow("gray")
  
# Performing OTSU threshold 
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
  
# Specify structure shape and kernel size.  
# Kernel size increases or decreases the area  
# of the rectangle to be detected. 
# A smaller value like (10, 10) will detect  
# each word instead of a sentence. 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
  
# Appplying dilation on the threshold image 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
  
# Finding contours 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                 cv2.CHAIN_APPROX_NONE) 
  
# Creating a copy of image 
im2 = img.copy() 

contours1 = sorted(contours, key=cv2.contourArea,reverse=True) 
# Select long perimeters only
perimeters = [cv2.arcLength(contours1[i],True) for i in range(len(contours1))]
listindex=[i for i in range(15) if perimeters[i]>perimeters[0]/2]
numcards=len(listindex)
# Show image
imgcont = img.copy()
[cv2.drawContours(imgcont, [contours1[i]], 0, (0,255,0), 5) for i in listindex]
cv2.imshow("with_line", imgcont)
cv2.waitKey(0)

# A text file is created and flushed 
file = open("recognized.txt", "w+") 
file.write("") 
file.close() 
  
# Looping through the identified contours 
# Then rectangular part is cropped and passed on 
# to pytesseract for extracting text from it 
# Extracted text is then written into the text file 
for cnt in contours: 
    x, y, w, h = cv2.boundingRect(cnt) 
      
    # Drawing a rectangle on copied image 
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
      
    # Cropping the text block for giving input to OCR 
    cropped = im2[y:y + h, x:x + w] 
      
    # Open the file in append mode 
    file = open("recognized.txt", "a") 
      
    # Apply OCR on the cropped image 
    text = pytesseract.image_to_string(cropped) 
      
    # Appending the text into file 
    file.write(text) 
    file.write("\n") 
      
    # Close the file 
    file.close 
