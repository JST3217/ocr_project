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
    # cv2.imshow('Img',Img)
    # cv2.waitKey(0)

    Img = Img[250:400, 175:545]  # cropping img to relevant parts

    Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)  # convert img to RGB
    white_px = (255, 255, 255)

    x1 = 190
    x2 = 325
    Img[0:150, x1:x1+40] = white_px  # remove useless stuff between readings
    Img[0:150, x2:x2+40] = white_px  # remove useless stuff between readings
    Img = Image.fromarray(Img)  # build img from array
    Img = cv2.cvtColor(np.array(Img), cv2.COLOR_RGB2BGR)

    scale_percent = 220  # percent of original size
    width = int(Img.shape[1] * scale_percent / 100)
    height = int(Img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(Img, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow('Img', resized)

    # Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # convert img to grayscale

    # thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # dilation
    def dilate(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.dilate(image, kernel, iterations=1)
    # im_dilated = dilate(Img)
    # im_bw = thresholding(Img)

    # custom_config = '--psm 4 --oem 3 outputbase digits'
    custom_config = '--psm 4 --oem 3 stdout -c tessedit_char_whitelist=-.?xmv0123456789 outputbase digits'
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

