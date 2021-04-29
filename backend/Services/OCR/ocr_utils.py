#link interessante https://nanonets.com/blog/ocr-with-tesseract/
import os

import cv2
import pytesseract

def extair_texto(file):
    a=os.getcwd()
    print(file)
    img = cv2.imread(file)

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    return(pytesseract.image_to_string(img, config=custom_config))
