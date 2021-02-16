import pytesseract
import os
import cv2
import re
from scipy import ndimage


def rotate(image, center = None, scale = 1.0):
    angle=360-int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

imPath = 'output.jpg'
img = cv2.imread(str(imPath), cv2.IMREAD_COLOR)
newdata=pytesseract.image_to_osd(img)
print(newdata)
angle = re.search('(?<=Rotate: )\d+', newdata).group(0)
print("angle: ", angle)
im = ndimage.rotate(img, float(angle) * -1)
im1 = rotate(img)

result = pytesseract.image_to_string(im)
fle= open("output.txt", "w", encoding='utf-8')
print(result, file = fle)