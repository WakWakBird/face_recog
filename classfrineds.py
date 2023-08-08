import face_recognition
import numpy as np
import cv2

class CameraTracer:
    def __init__(self, index):
        self.index = index
        self.num_cameras = 0
        self.inputed_camera = 0
        self.capture = 0

    def count_connected_cameras(self):
        index = self.index
        while True:
            self.capture = cv2.VideoCapture(index)
            if not self.capture.isOpened():
                break
            self.num_cameras += 1
            self.capture.release()
            index += 1
        return self.num_cameras 
    
    def camera_input(self, inputed_camera):
        self.inputed_camera = inputed_camera

    def camera_designate(self):
        if self.inputed_camera <= self.num_cameras:
            print(f"{self.inputed_camera - 1}번 카메라를 지정합니다.")
        elif self.inputed_camera >= self.num_cameras:
            print(f"{self.num_cameras + 1} 번 이상 카메라는 사용할 수 없습니다...") 
            return False

class FacePredict:
    def __init__(self, user_input):
        self.tracer = CameraTracer(0)
        self.tracer.capture = cv2.VideoCapture(user_input - 1)

        # Load known faces
        image1 = face_recognition.load_image_file("KIM.jpg")
        encoding1 = face_recognition.face_encodings(image1)[0]

        image2 = face_recognition.load_image_file("SON.jpg")
        encoding2 = face_recognition.face_encodings(image2)[0]

        self.known_face_encodings = [encoding1, encoding2]
        self.known_face_names = ["Min-Jae KIM", "Heung-Min SOn"]

    def predict_faces(self):
        while True:
            ret, frame = self.tracer.capture.read()

            # Find all face locations using face_recognition library
            face_locations = face_recognition.face_locations(frame, model="hog")
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                if any(matches):
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.tracer.capture.release()
        cv2.destroyAllWindows()

