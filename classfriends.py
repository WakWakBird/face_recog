import os
import face_recognition
import numpy as np
import cv2


class WebcamTracer:
    def __init__(self, index):
        self.index = index
        self.num_cameras = 0

    def count_connected_cameras(self):
        index = self.index
        while True:
            capture = cv2.VideoCapture(index)
            if not capture.isOpened():
                break
            self.num_cameras += 1
            capture.release()
            index += 1
        return self.num_cameras
if __name__ == "__main__":
    webcam = WebcamTracer(0)  # Webcam 클래스의 인스턴스를 생성하고, index 값으로 0을 전달하여 초기화
    num_cameras = webcam.count_connected_cameras()
    print(f"컴퓨터에 연결된 카메라 개수: {num_cameras}개")     


class CameraDesignate:
    def __init__(self):
        self.camera_number = 0
        self.inputed_camera = 0  # 초기 속성 0으로 부여
    
    def camera_designation(self, camera_number):
        self.camera_number = camera_number

    def camera_input(self, inputed_cameras):
        self.inputed_camera = inputed_cameras
    
    def user_camera_input(self):
        int(input("사용하고 싶은 카메라 개수를 입력하세요"))
        
    def compare_and_designate(self):
        if self.inputed_camera <= self.camera_number:
            print(f"{self.inputed_camera}개의 카메라를 지정합니다.")
        elif self.inputed_camera >= self.camera_number:
            print(f"{self.camera_number}개 이상의 카메라는 지정할 수 없습니다.") 
        else:
            print("오류오류오류오류!")

if __name__ == "__main__":
    webcam = WebcamTracer(0)  # WebcamTracer 클래스의 인스턴스를 생성하고, index 값으로 0을 전달하여 초기화
    num_cameras = webcam.count_connected_cameras()  

    serviceable_camera = CameraDesignate()

    serviceable_camera.camera_designation(num_cameras)  # webcam instance의 num_cameras 속성을 전달하여 메서드 호출

    user_input = int(input("지정할 카메라 개수를 입력하세요: "))
    serviceable_camera.camera_input(user_input)

    serviceable_camera.compare_and_designate()


class FaceMatcher:
    def __init__(self, image_filename):
        self.image_to_be_matched = face_recognition.load_image_file(image_filename)
        self.image_to_be_matched_encoded = face_recognition.face_encodings(self.image_to_be_matched)[0]
        self.images = os.listdir('images')

    def match_faces(self):
        for image in self.images:
            current_image = face_recognition.load_image_file("images/" + image) 
            #여기서 self.images가 인자로 사용되는 것이 아닌 load_image_file에서 image파일 경로만 추가했기 때문임
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
            result = face_recognition.compare_faces([self.image_to_be_matched_encoded], current_image_encoded)
            #여기는 self.image_to_be_matched_encoded 을 인자로 사용하기 때문에 self.까지 명시를 해주어야 함.
            if result[0]:
                print("Matched: " + image)
            else:  
                print("Not matched: " + image)

if __name__ == "__main__":
    face_matcher = FaceMatcher('my_image.jpg')
    face_matcher.match_faces()