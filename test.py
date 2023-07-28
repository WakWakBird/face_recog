import cv2
import numpy as np


class Webcam:
  
    def __init__(self,index):
        self.index = index

    def count_connected_cameras():
        num_cameras = 0
        index = 0
        while True : 
            capture = cv2.VideoCapture(index)
            if not capture.isOpened():
                break
            num_cameras += 1
            capture.release()
            index += 1
        return num_cameras
    
    num_cameras = count_connected_cameras()
    print(num_cameras)