import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerlimit = hsv_color[0][0][0] - 10, 100, 100
    upperlimit = hsv_color[0][0][0] + 10, 255, 255

    lowerlimit = np.array(lowerlimit, dtype=np.uint8)   
    upperlimit = np.array(upperlimit, dtype=np.uint8)

    return lowerlimit, upperlimit
   