import cv2 as cv
import numpy as np
import pygetwindow
import mss
import traceback
import os
from PIL import Image

def get_screenshot():
    try:
        windows = pygetwindow.getActiveWindow()
        print("Windows Title", windows.title)
        window_ets2 = pygetwindow.getWindowsWithTitle("Euro Truck Simulator 2 Multiplayer")[0]
        #get win location and size
        top, left, width, height = window_ets2.top, window_ets2.left, window_ets2.width, window_ets2.height
        monitor = {"top": top, "left": left, "width":width, "height":height}

        with mss.mss() as sct:
            sct_img = sct.shot()
            sct_shot = Image.open(sct_img)
            np_data = np.asarray(sct_shot)
            np_data = cv.cvtColor(np_data, cv.COLOR_RGB2BGR)
            cv.waitKey(0)
        return np_data
    except IndexError:
        print("Window not found")
    except Exception as e:
        traceback.print_exc()
