import cv2
import numpy
import matplotlib
import pytesseract as tess

# function to build: for each item in Reports, save the name, then construct img path
img_path = 'Reports/' + 'Report_210810_082307' + '/MU_Main_Tab_0_Analog.png'
Img = cv2.imread(img_path)

# h, w, _ = Img.shape
Img = Img[250:400, 175:545]  # cropping img to relevant parts
img.setTo(Scalar::all(0),mask)
# function to build: opencv to remove unused text between the reading

Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # convert img to grayscale

#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#dilation
def dilate(image):
    kernel = numpy.ones((5,5),numpy.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

# im_dilated = dilate(Img)
# im_bw = thresholding(Img)

custom_config = '--psm 4 --oem 3 outputbase digits'
# custom_config = '--psm 4 --oem 3 stdout -c tessedit_char_whitelist=-.?xmvV0123456789 outputbase digits'
text = tess.image_to_string(Img, config=custom_config)  #pass img to tess with whitelist char
# text = tess.image_to_string(im_bw, config='--psm 4 stdout -c tessedit_char_whitelist=-.?mV0123456789')  #pass img to tess with whitelist char

print(text)  # currently grey works better than BW

cv2.imshow('Gray image', Img)
# cv2.imshow('dilate image', im_dilated)
cv2.imshow('BW image', im_bw)
cv2.waitKey(0)
