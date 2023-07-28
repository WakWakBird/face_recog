import os
import face_recognition

class FaceMatcher:
    def __init__(self, image_filename):
        self.image_to_be_matched = face_recognition.load_image_file(image_filename)
        self.image_to_be_matched_encoded = face_recognition.face_encodings(self.image_to_be_matched)[0]
        self.images = os.listdir('images')

    def match_faces(self):
        for image in self.images:
            current_image = face_recognition.load_image_file("images/" + image)
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
            result = face_recognition.compare_faces([self.image_to_be_matched_encoded], current_image_encoded)
            if result[0]:
                print("Matched: " + image)
            else:
                print("Not matched: " + image)

if __name__ == "__main__":
    face_matcher = FaceMatcher('my_image.jpg')
    face_matcher.match_faces()


