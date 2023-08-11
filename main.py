from classfriends import *

cameratracer = CameraTracer(0)
num_camera = cameratracer.count_connected_cameras()
print(f"컴퓨터에 연결된 카메라 개수: {num_camera}개")
user_input = int(input("지정할 카메라를 입력하세요: "))
cameratracer.camera_input(user_input)
cameratracer.camera_designate()


facepredict = FacePredict(user_input,
                              ("KIM.jpg", "Min-Jae Kim"),
                              ("SON.jpg","Heung-Min Son"),
                              ("CR7.jpg","Cristiano_Ronaldo"),
                              ("Emerson.jpg","Emerson_Royal"),
                              ("Karim_Benzema.jpg","Karim_Benzema"),
                              ("Harry_Kane.jpg","Harry_Kane"),
                              ("GOAT.jpg","Lionel_Messi"),
                              ("gay.jpg","Hyeon-Yup Jeon")
                              )
facepredict.predict_faces()
