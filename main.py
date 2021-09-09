import cv2
from PIL import Image
import numpy as np
import matplotlib
import pytesseract as tess
import os

in_filename = 'MU_Main_Tab_0_Analog.png'  # only look at this img file
folderPath = 'Reports'
myRobots = os.listdir(folderPath)  # get robot directory name

robot_counter = 0
img_path = []

for reports in myRobots:
    reports = os.listdir(folderPath + '/' + reports)
    for report in reports:
        img_path.append(folderPath + '/' + myRobots[robot_counter] + '/' + report + '/' + in_filename)
    robot_counter = robot_counter + 1

for img in img_path:
    Img = cv2.imread(img)

    Img = Img[250:400, 175:545]  # cropping img to relevant parts

    Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)  # convert img to RGB
    white_px = (255, 255, 255)

    x1 = 190
    x2 = 325
    Img[0:150, x1:x1+40] = white_px  # remove useless stuff between readings
    Img[0:150, x2:x2+40] = white_px  # remove useless stuff between readings
    Img = Image.fromarray(Img)  # build img from array
    Img = cv2.cvtColor(np.array(Img), cv2.COLOR_RGB2BGR)

    scale_percent = 250  # percent of original size
    width = int(Img.shape[1] * scale_percent / 100)
    height = int(Img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    Img = cv2.resize(Img, dim, interpolation=cv2.INTER_AREA)


    def gray(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # thresholding # pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    def thresholding(image):
        return cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]

    # erosion, similar to bold
    def erode(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.erode(image, kernel, iterations=1)

    # dilation == thinner
    def dilate(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.dilate(image, kernel, iterations=1)

    def debug(Img):
        cv2.imshow('Img', Img)
        cv2.waitKey(0)

    Img = gray(Img)
    debug(Img)
    Img = thresholding(Img)
    debug(Img)
    # Img = dilate(Img)
    # debug(Img)
    # Img = erode(Img)
    # debug(Img)
    # Img = dilate(Img)
    # debug(Img)

    contours, _ = cv2.findContours(Img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    # def contours_text(orig, Img, contours):
    #     for cnt in contours:
    #         x, y, w, h = cv2.boundingRect(cnt)
    #
    #         # Drawing a rectangle on copied image
    #         rect = cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 255), 2)
    #
    #         cv2.imshow('cnt', rect)
    #         cv2.waitKey()
    #
    #         # Cropping the text block for giving input to OCR
    #         cropped = orig[y:y + h, x:x + w]
    #
    #         # Apply OCR on the cropped image
    #         config = ('-l eng --oem 1 --psm 3')
    #         text = pytesseract.image_to_string(cropped, config=config)
    #
    #         print(text)


    # custom_config = '--psm 4 --oem 3 outputbase digits'
    custom_config = '--psm 4 --oem 3 stdout -c tessedit_char_whitelist=-0123456789.?xmv outputbase digits'
    text = tess.image_to_string(Img, config=custom_config)  # pass img to tess with whitelist char
    # text = tess.image_to_string(im_bw, config='--psm 4 stdout -c tessedit_char_whitelist=-.?mV0123456789')  #pass img to tess with whitelist char

    out_filename = img[8:26] + '_' + img[27:47]
    out_filepath = 'Outputs/Raw/'+out_filename+'.txt'
    print(text,  file=open(out_filepath, 'w'))

    with open(out_filepath) as infile, open('Outputs/Processed/'+out_filename+'.txt', 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output

    f = open('Outputs/Processed/'+out_filename+'.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

    cv2.waitKey(0)

