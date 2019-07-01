import pickle

with open('Files/dataset_faces.dat', 'rb') as f:
    all_face_encodings = pickle.load(f)

face_names = list(all_face_encodings.keys())
#face_encodings =np.array(list(all_face_encodings.values()))

for x in face_names:
    print(x)
