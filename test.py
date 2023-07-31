import cv2
import numpy as np
from classfriends import CameraTracer

class CameraDesignate:
    def __init__(self):
        self.camera_number = 0
        self.inputed_camera = 0  # 초기 속성 0으로 부여
    
    def camera_designation(self, camera_number):
        self.camera_number = camera_number

    def camera_input(self, inputed_cameras):
        self.inputed_camera = inputed_cameras
    
    def compare_and_designate(self):
        if self.inputed_camera <= self.camera_number:
            print(f"{self.inputed_camera}번 카메라를 지정합니다.")
            capture = cv2.VideoCapture(self.inputed_camera - 1)
            if capture.isOpened():
                capture.release()
                return True
            else:
                return False

        elif self.inputed_camera >= self.camera_number:
            print(f"{self.camera_number + 1} 번 이상 카메라는 사용할 수 없습니다..") 
            return False

        else:
            print("오류오류오류오류!")
            return False

if __name__ == "__main__":
    webcam = CameraTracer(0)  # WebcamTracer 클래스의 인스턴스를 생성하고, index 값으로 0을 전달하여 초기화
    num_cameras = webcam.count_connected_cameras()  

    serviceable_camera = CameraDesignate()

    serviceable_camera.camera_designation(num_cameras)  # webcam instance의 num_cameras 속성을 전달하여 메서드 호출

    user_input = int(input("지정할 카메라 개수를 입력하세요: "))
    
    serviceable_camera.camera_input(user_input)

    if serviceable_camera.compare_and_designate():
        print("카메라가 연결되었습니다.")
    else:
        print("카메라가 연결되지 않았습니다.")
