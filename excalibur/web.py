from flask import Flask, render_template, redirect, url_for, request,session
from backend import *
import os
from face_dataset import *
import pickle
from PIL import Image, ImageDraw
app=Flask(__name__)

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

@app.route('/')
def home():
    return "Welcome"

#@app.route('/about/')
#def about():
#    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        row=search(request.form['username'],request.form['password'])
        if not row:
            error = 'Invalid Credentials. Please try again.'
        else:
            if not os.path.exists(row[0][2]):
                os.mkdir(row[0][2])
                os.chdir(row[0][2])
                os.mkdir("test")
                os.chdir("../..")
                UPLOAD_FOLDER = row[0][2]+"/test"




            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form["cpassword"]:
            error = 'Passwords do not match!'
        elif search1(request.form['username']):
            error='username exists!'


        else:
            insert(request.form['name'],request.form['username'],request.form['email'],request.form['dob'],request.form['password'])
            r=request.form['username']
            if not os.path.exists(r):
                os.mkdir(r)
                os.chdir(r)
                os.mkdir("test")
                os.chdir("..")
                UPLOAD_FOLDER = r+"/test"
                app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                file = request.files['image']
                f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(f)
            myfun(request.form['name'],request.form['username'])
            with open('Files/dataset_faces.dat', 'rb') as f:
                all_face_encodings = pickle.load(f)
            image=face_recognition.load_image_file(request.form['username']+"/"+request.form['username']+"0.jpg")
                #image1=face_recognition.load_image_file("6.jpg")
            face_locations = face_recognition.face_locations(image)
            test_face = face_recognition.face_encodings(image, face_locations)
            pil_image = Image.fromarray(image)
            pil_image1 = Image.fromarray(image)
            draw = ImageDraw.Draw(pil_image)
            for (top, right, bottom, left) in face_locations:
                draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            pil_image.show()
            all_face_encodings[request.form['username']+"("+request.form['name']+")"]=test_face
            with open('Files/dataset_faces.dat', 'wb') as f:
                pickle.dump(all_face_encodings, f)
            return redirect(url_for('login'))

    return render_template('register.html', error=error)

if __name__=="__main__":
    app.run(debug=True)
