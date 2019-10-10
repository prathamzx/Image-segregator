import face_recognition
import cv2
import os


def myfun(name,username):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        #cv2.circle(,(447,63), 63, (0,0,255), -1)
        ret, frame = cam.read()
        frame = cv2.flip(frame,1)
        cv2.rectangle(img=frame, pt1=(170, 100), pt2=(430, 350), color=(255, 0, 255), thickness=1, lineType=8, shift=0)
        cv2.imshow("test", frame)

        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = (username+str(img_counter))+".jpg"
            os.chdir(username)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            x=username+"("+name+")"
            if not os.path.exists(x):
                os.mkdir(x)
            os.chdir("..")
            img_counter += 1
            #this is a image counter

    cam.release()

    cv2.destroyAllWindows()
