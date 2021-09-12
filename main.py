import os

import numpy as np
from PIL import Image
from numpy import load
import glob


def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()


def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(round(time.time() - startTime_for_tictoc)) + " seconds.")
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


def char2txt(x):
    return {
        'char_lib\\char_0_array.npy': '0',
        'char_lib\\char_1_array.npy': '1',
        'char_lib\\char_2_array.npy': '2',
        'char_lib\\char_3_array.npy': '3',
        'char_lib\\char_4_array.npy': '4',
        'char_lib\\char_5_array.npy': '5',
        'char_lib\\char_6_array.npy': '6',
        'char_lib\\char_7_array.npy': '7',
        'char_lib\\char_8_array.npy': '8',
        'char_lib\\char_9_array.npy': '9',
        'char_lib\\char_dot_array.npy': '.',
        'char_lib\\char_m_array.npy': 'm',
        'char_lib\\char_neg_array.npy': '-',
        'char_lib\\char_que_array.npy': '?',
        'char_lib\\char_V_array.npy': 'V',
    }.get(x, 'ERROR')


def blank_rec(current_blank_array, myChars):
    current_blank_value = []
    for i in range(current_blank_array.shape[1]):  # each col in blank
        for char in myChars:  # loop through each char
            current_char_array = load(char)
            if current_blank_array.shape[1] - i > current_char_array.shape[
                1]:  # if remaining cols to investigate > current char col
                inv_array = current_blank_array[0:current_char_array.shape[0],
                            i:i + current_char_array.shape[1]]  # crop remaining cols to char sizet
                if np.allclose(current_char_array, inv_array, atol=35):  # if match with current char
                    current_blank_value.append(char2txt(char))  # append to current blank value
    return ''.join(current_blank_value)  # combine array of char to single string


myChars = []
for char in glob.glob('char_lib/*.npy'):
    myChars.append(char)  # array of paths to all chars

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
    tic()
    Img_array = np.array(Image.open(img).convert('L'))
    # show_img(img)
    box_shape = (17, 56)

    sc_sin_master_array = Img_array[261:261 + box_shape[0], 303:303 + box_shape[1]]
    sc_cos_master_array = Img_array[309:309 + box_shape[0], 303:303 + box_shape[1]]
    sc_pha_master_array = Img_array[357:357 + box_shape[0], 303:303 + box_shape[1]]
    sc_sin_nonius_array = Img_array[261:261 + box_shape[0], 435:435 + box_shape[1]]
    sc_cos_nonius_array = Img_array[309:309 + box_shape[0], 435:435 + box_shape[1]]
    sc_pha_nonius_array = Img_array[357:357 + box_shape[0], 435:435 + box_shape[1]]

    text = ['Signal Conditioning Master Sine Offset: ' + blank_rec(sc_sin_master_array, myChars),
            'Signal Conditioning Master Cosine Offset: ' + blank_rec(sc_cos_master_array, myChars),
            'Signal Conditioning Master Phase Adjust: ' + blank_rec(sc_pha_master_array, myChars),
            'Signal Conditioning Nonius Sine Offset: ' + blank_rec(sc_sin_nonius_array, myChars),
            'Signal Conditioning Nonius Cosine Offset: ' + blank_rec(sc_cos_nonius_array, myChars),
            'Signal Conditioning Nonius Phase Adjust: ' + blank_rec(sc_pha_nonius_array, myChars)]

    out_filename = img[8:26] + '_' + img[27:47]
    out_filepath = 'Outputs/' + out_filename + '.txt'

    with open(out_filepath, 'w') as txt_file:
        for line in text:
            txt_file.write(''.join(line) + "\n")

    toc()
