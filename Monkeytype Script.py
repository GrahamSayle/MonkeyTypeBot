import cv2
import numpy as np
import keyboard
import mss
from pytesseract import pytesseract
from time import sleep


pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Dimensions of each line
dim1 = {
    'left': 158,
    'top': 488,
    'width': 1590,
    'height': 55
}

dim2 = {
    'left': 158,
    'top': 546,
    'width': 1590,
    'height': 55
}

dim3 = {
    'left': 158,
    'top': 608,
    'width': 1590,
    'height': 55
}
dims = [dim1,dim2,dim3,dim3,dim3,dim3,dim3,dim3]

mss = mss.mss()

keyboard.wait("shift")

# Typing out the characters seen in each line, sleep is the delay in between writing words
for dim in dims:
    scr = np.array(mss.grab(dim))
    words = pytesseract.image_to_string(scr)
    if dim == dim1 and (words[0] == "l" or words[0] == "{"):
        words = words[1:]
    print(words)
    for word in words:
        keyboard.write(word)
        #sleep(0.025)
    keyboard.write(" ")



