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


class FaceRecognizer:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

    def load_known_faces(self, image_files_and_names):
        for image_file, name in image_files_and_names:
            image = face_recognition.load_image_file(image_file)
            face_encoding = face_recognition.face_encodings(image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(name)

    def recognize_faces(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            if any(matches):
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
            print(f"Detected face: {name}, Location: ({top}, {right}, {bottom}, {left})")


class FacePredict:
    def __init__(self, user_input, *known_faces):
        self.tracer = CameraTracer(0)
        self.tracer.capture = cv2.VideoCapture(user_input - 1)
        self.recognizer = FaceRecognizer()

        if known_faces:
            self.recognizer.load_known_faces(known_faces)

    def predict_faces(self):
        while True:
            ret, frame = self.tracer.capture.read()
            if not ret:
                break

            self.recognizer.recognize_faces(frame)
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.tracer.capture.release()
        cv2.destroyAllWindows()


