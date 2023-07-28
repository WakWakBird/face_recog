import os
import face_recognition
import numpy as np
import cv2

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


face_matcher = FaceMatcher('my_image.jpg')
face_matcher.match_faces()

class camera_number:
    def __init__(self):
        capture =  cv2.VidioCapture(0)

      



