import numpy as np
import cv2
import time

from directkeys import PressKey, ReleaseKey, W, A, S, D


from draw_lanes import draw_lanes
from grabscreen import grab_screen
from getkeys import key_check
import os

def keys_to_output(keys):
    #[A,W,D]
    output  = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1

    return output 



#input
#PressKey(W)
#time.sleep(3)
#PressKey(W)

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previos data')
    training_data = list(np.load(file_name))
else:
    print('File does not exist , starting fresh')
    training_data = []



last_time = time.time()

for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)
 

while True:
        screen = grab_screen(region=(0,40,800,600))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen,(80,60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        
        
        print('Loop took {}'.format(time.time()-last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

        
