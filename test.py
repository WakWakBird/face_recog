import cv2
import numpy as np


class Webcam:
    def __init__(self, index):
        self.index = index

    def count_connected_cameras(self):
        num_cameras = 0
        index = self.index
        while True:
            capture = cv2.VideoCapture(index)
            if not capture.isOpened():
                break
            num_cameras += 1
            capture.release()
            index += 1
        return num_cameras

webcam = Webcam(0)  # Webcam 클래스의 인스턴스를 생성하고, index 값으로 0을 전달하여 초기화
num_cameras = webcam.count_connected_cameras()
print(f"컴퓨터에 연결된 카메라 개수: {num_cameras}개")