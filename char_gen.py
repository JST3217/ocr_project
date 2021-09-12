import os

import numpy as np
from numpy import save
from PIL import Image


def save_char2img(img_array, spec):
    filename = spec
    filepath = 'char_lib/' + filename + '.png'
    Image.fromarray(img_array).save(filepath)
    return filepath


def show_img(filepath):
    img = Image.open(filepath)
    img.show()


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

box_shape = (17, 56)

img = img_path[0]
show_img(img)
Img_array = np.array(Image.open(img).convert('RGB'))
# Img_array = np.array(Image.open(img).convert('L'))  # grayscale

char_1_array = Img_array[357:357 + box_shape[0], 462:467]  # img_path[0]
save('char_lib/char_1_array.npy', char_1_array)
char_1 = save_char2img(char_1_array, 'char_1')

char_3_array = Img_array[261:261 + box_shape[0], 315:322]  # img_path[0]
save('char_lib/char_3_array.npy', char_3_array)
char_3 = save_char2img(char_3_array, 'char_3')

char_4_array = Img_array[357:357 + box_shape[0], 468:474]  # img_path[0]
save('char_lib/char_4_array.npy', char_4_array)
char_4 = save_char2img(char_4_array, 'char_4')

char_6_array = Img_array[357:357 + box_shape[0], 322:329]  # img_path[0]
save('char_lib/char_6_array.npy', char_6_array)
char_6 = save_char2img(char_6_array, 'char_6')

char_7_array = Img_array[357:357 + box_shape[0], 454:461]  # img_path[0]
save('char_lib/char_7_array.npy', char_7_array)
char_7 = save_char2img(char_7_array, 'char_7')

img = img_path[1]
show_img(img)
Img_array = np.array(Image.open(img).convert('RGB'))
# Img_array = np.array(Image.open(img).convert('L'))  # grayscale


char_5_array = Img_array[357:357 + box_shape[0], 454:461]  # img_path[1]
save('char_lib/char_5_array.npy', char_5_array)
char_5 = save_char2img(char_5_array, 'char_5')

char_8_array = Img_array[357:357 + box_shape[0], 329:336]  # img_path[1]
save('char_lib/char_8_array.npy', char_8_array)
char_8 = save_char2img(char_8_array, 'char_8')

img = img_path[2]
show_img(img)
Img_array = np.array(Image.open(img).convert('RGB'))
# Img_array = np.array(Image.open(img).convert('L'))  # grayscale

char_0_array = Img_array[309:309 + box_shape[0], 315:322]  # img_path[2]
save('char_lib/char_0_array.npy', char_0_array)
char_0 = save_char2img(char_0_array, 'char_0')

char_2_array = Img_array[261:261 + box_shape[0], 315:322]  # img_path[2]
save('char_lib/char_2_array.npy', char_2_array)
char_2 = save_char2img(char_2_array, 'char_2')

char_dot_array = Img_array[357:357 + box_shape[0], 319:321]  # img_path[2]
save('char_lib/char_dot_array.npy', char_dot_array)
char_dot = save_char2img(char_dot_array, 'char_dot')

char_neg_array = Img_array[357:357 + box_shape[0], 307:310]  # img_path[2]
save('char_lib/char_neg_array.npy', char_neg_array)
char_neg = save_char2img(char_neg_array, 'char_neg')

char_que_array = Img_array[357:357 + box_shape[0], 347:353]  # img_path[2]
save('char_lib/char_que_array.npy', char_que_array)
char_que = save_char2img(char_que_array, 'char_que')

char_m_array = Img_array[261:261 + box_shape[0], 327:337]  # img_path[2]
save('char_lib/char_m_array.npy', char_m_array)
char_m = save_char2img(char_m_array, 'char_m')

char_V_array = Img_array[261:261 + box_shape[0], 337:346]  # img_path[2]
save('char_lib/char_V_array.npy', char_V_array)
char_V = save_char2img(char_V_array, 'char_V')

img = img_path[3]
show_img(img)
Img_array = np.array(Image.open(img).convert('RGB'))
# Img_array = np.array(Image.open(img).convert('L'))  # grayscale

char_9_array = Img_array[357:357 + box_shape[0], 327:334]  # img_path[3]
save('char_lib/char_9_array.npy', char_9_array)
char_9 = save_char2img(char_9_array, 'char_9')













