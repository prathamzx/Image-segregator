import face_recognition
from PIL import Image, ImageDraw
import os,glob,shutil
import sqlite3
import pickle
import numpy as np

names_with_result="no faces detected"

os.chdir("../test7/test")
for images in glob.glob("*.jpg"):
    with open('../../Files/dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)
    face_names = list(all_face_encodings.keys())
    face_encodings =np.array(list(all_face_encodings.values()))
    image_name=images
    image=face_recognition.load_image_file(images)
        #image1=face_recognition.load_image_file("6.jpg")
    face_locations = face_recognition.face_locations(image)
    test_face = face_recognition.face_encodings(image, face_locations)
        #test_face1 = face_recognition.face_encodings(image1)
    pil_image = Image.fromarray(image)
    pil_image1 = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    pil_image.show()

    for face in test_face:
        name=""
        print(face)
        print(all_face_encodings)
        result = face_recognition.compare_faces(face_encodings,face)
        print(face)
        print(face_encodings)
        names_with_result = list(zip(face_names, result))
        i=0
        for x,y in names_with_result:
            i=i+1
            if y==True:
                name=x
                os.chdir("..")
                if not os.path.exists(name):
                    os.mkdir(name)
                os.chdir(name)
                pil_image1.save(image_name)
                os.chdir("../test")

        if name=="":
            os.chdir("..")
            name=input("Enter name of the person:")
            os.mkdir(name)
            os.chdir(name)
            pil_image1.save(image_name)
            all_face_encodings[name]=face
            os.chdir("..")
            with open('../Files/dataset_faces.dat', 'wb') as f:
                pickle.dump(all_face_encodings, f)
            os.chdir("test")

print(names_with_result)
