import os

import numpy as np
from PIL import Image
from numpy import save, load


def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()


def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")


def gen_directory(dirlist):  # fn to create directories
    directories = open(dirlist).read().split('\n')
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError:
            print("Directory '%s' can not be created" % directory)


def save_array2img(img_array, source_path, spec):
    filename = source_path[8:26] + '_' + source_path[27:47] + '_' + spec
    filepath = 'Outputs/Images/' + filename + '.png'
    Image.fromarray(img_array).save(filepath)
    return filepath


def save_char2img(img_array, spec):
    filename = spec
    filepath = 'char_lib/' + filename + '.png'
    Image.fromarray(img_array).save(filepath)
    return filepath


def show_img(filepath):
    img = Image.open(filepath)
    img.show()


gen_directory('directory.txt')  # create output directory

in_filename = 'MU_Main_Tab_0_Analog.png'  # only look at this img file
folderPath = 'Reports'
myRobots = os.listdir(folderPath)  # get robot(s) directory name

robot_counter = 0
img_path = []

# get img file path for all img
for reports in myRobots:
    reports = os.listdir(folderPath + '/' + reports)
    for report in reports:
        img_path.append(folderPath + '/' + myRobots[robot_counter] + '/' + report + '/' + in_filename)
    robot_counter = robot_counter + 1


for img in img_path:
    Img_array = np.array(Image.open(img).convert('L'))

    box_shape = (17, 56)

    sc_sin_master_array = Img_array[261:261 + box_shape[0], 303:303 + box_shape[1]]
    sc_cos_master_array = Img_array[309:309 + box_shape[0], 303:303 + box_shape[1]]
    sc_pha_master_array = Img_array[357:357 + box_shape[0], 303:303 + box_shape[1]]
    sc_sin_nonius_array = Img_array[261:261 + box_shape[0], 435:435 + box_shape[1]]
    sc_cos_nonius_array = Img_array[309:309 + box_shape[0], 435:435 + box_shape[1]]
    sc_pha_nonius_array = Img_array[357:357 + box_shape[0], 435:435 + box_shape[1]]

    sc_sin_master = save_array2img(sc_sin_master_array, img, 'sc_sin_master')
    sc_cos_master = save_array2img(sc_cos_master_array, img, 'sc_cos_master')
    sc_pha_master = save_array2img(sc_pha_master_array, img, 'sc_pha_master')
    sc_sin_nonius = save_array2img(sc_sin_nonius_array, img, 'sc_sin_nonius')
    sc_cos_nonius = save_array2img(sc_cos_nonius_array, img, 'sc_cos_nonius')
    sc_pha_nonius = save_array2img(sc_pha_nonius_array, img, 'sc_pha_nonius')
