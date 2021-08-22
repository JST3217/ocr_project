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
Img = Img[250:400, 175:545]  # cropping img to relevant parts

# opencv to remove unused text between the reading

Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # convert img to grayscale

thresh = 200  # experiment for suitable threshold
im_bw = cv2.threshold(Img, thresh, 255, cv2.THRESH_BINARY)[1]

text = tess.image_to_string(Img, config='--psm 4 stdout -c tessedit_char_whitelist=-.?xmvV0123456789')  #pass img to tess with whitelist char
# text = tess.image_to_string(im_bw, config='--psm 4 stdout -c tessedit_char_whitelist=-.?mV0123456789')  #pass img to tess with whitelist char

print(text)  # currently grey works better than BW

cv2.imshow('Gray image', Img)
cv2.imshow('BW image', im_bw)
cv2.waitKey(0)