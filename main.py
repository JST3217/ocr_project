import cv2
import numpy
import matplotlib
import pytesseract as tess

# function to build: for each item in Reports, save the name, then construct img path
img_path = 'Reports/' + 'Report_210810_082307' + '/MU_Main_Tab_0_Analog.png'
Img = cv2.imread(img_path)

h, w, _ = Img.shape
y = 250
x = 290
Img = Img[y:y + 150, x:x + 70]  # cropping img to relevant parts

Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # convert img to grayscale

text = tess.image_to_string(Img, config='--psm 6 stdout -c tessedit_char_whitelist=-.?mV0123456789')  #pass img to tess with whitelist char
print(text)

cv2.imshow('Gray image', Img)
cv2.waitKey(0)