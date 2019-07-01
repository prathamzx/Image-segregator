import face_recognition
import pickle

all_face_encodings = {}

img1 = face_recognition.load_image_file("srk.jpg")
all_face_encodings["srk"] = face_recognition.face_encodings(img1)[0]

img2 = face_recognition.load_image_file("test4.jpg")
all_face_encodings["elvis"] = face_recognition.face_encodings(img2)[0]



#print(all_face_encodings)
with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)
