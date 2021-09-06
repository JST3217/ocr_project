import cv2
from PIL import Image
import numpy as np
import matplotlib
import pytesseract as tess

# function to build: for each item in Reports, save the name, then construct img path

# img_path = 'Reports/' + 'Report_210810_082307' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/' + 'Report_210810_143330' + '/MU_Main_Tab_0_Analog.png'

# img_path = 'Reports/EV4.15U01-2128-002/' + 'Report_210712_141129' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/EV4.15U01-2128-002/' + 'Report_210712_164050' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/EV4.15U01-2128-002/' + 'Report_210713_081243' + '/MU_Main_Tab_0_Analog.png'
img_path = 'Reports/EV4.15U01-2128-002/' + 'Report_210713_123928' + '/MU_Main_Tab_0_Analog.png'

# img_path = 'Reports/EV4.15U01-2129-002/' + 'Report_210720_081826' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/EV4.15U01-2129-002/' + 'Report_210720_085549' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/EV4.15U01-2129-002/' + 'Report_210720_090241' + '/MU_Main_Tab_0_Analog.png'
# img_path = 'Reports/EV4.15U01-2129-002/' + 'Report_210720_090920' + '/MU_Main_Tab_0_Analog.png'

Img = cv2.imread(img_path)

cv2.imshow('Img',Img)
cv2.waitKey(0)

Img = Img[250:400, 175:545]  # cropping img to relevant parts

cv2.imshow('Img',Img)
cv2.waitKey(0)

Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)  # convert img to RGB
white_px = (255, 255, 255)
black_px = (0, 0, 0)

x1 = 190
x2 = 325
Img[0:150, x1:x1+40] = white_px  # remove useless stuff between readings
Img[0:150, x2:x2+40] = white_px  # remove useless stuff between readings
Img = Image.fromarray(Img)  # build img from array

# Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # convert img to grayscale

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# dilation
def dilate(image):
    kernel = numpy.ones((5, 5), numpy.uint8)
    return cv2.dilate(image, kernel, iterations=1)
# im_dilated = dilate(Img)
# im_bw = thresholding(Img)

# custom_config = '--psm 4 --oem 3 outputbase digits'
custom_config = '--psm 4 --oem 3 stdout -c tessedit_char_whitelist=-.?xmv0123456789 outputbase digits'
text = tess.image_to_string(Img, config=custom_config)  # pass img to tess with whitelist char
# text = tess.image_to_string(im_bw, config='--psm 4 stdout -c tessedit_char_whitelist=-.?mV0123456789')  #pass img to tess with whitelist char

print(text,  file=open('log.txt', 'w'))

with open('log.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

f = open('output.txt', 'r')
file_contents = f.read()
print (file_contents)
f.close()

Img.show()
# cv2.waitKey(0)
