import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
from imutils.video import VideoStream
import imutils
from scipy.spatial import distance as dist

frame = cv2.VideoCapture(0)
model = cv2.CascadeClassifier(os.path.join(os.getcwd(), 'lbpcascade_frontalface_improved.xml'))
maskNet = load_model(os.path.join(os.getcwd(), 'detect.model'))
labels = {0: 'MASK', 1: 'NO MASK'}
colors = {0: (0, 255, 0), 1: (0, 0, 255)}

while 1:

    _, pic = frame.read()
    
    # mask detection
    faces = model.detectMultiScale(pic)

    for (x, y, w, h) in faces:
        face = pic[y:y + w, x:x + w]
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        reshaped_img = np.reshape(face / 255, (1, 224, 224, 3))
        res = maskNet.predict(reshaped_img)
        label = int(res[0][0] <= 0.8 )

        cv2.rectangle(pic, (x, y), (x + w, y + h), colors[label], 2)
        cv2.rectangle(pic, (x, y - 40), (x + w, y), colors[label], -1)
        cv2.putText(pic, labels[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

    # social distancing
    length = len(faces)
    pic = cv2.putText(pic, str(len(faces)) + " Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                      1, (255, 0, 0), 2, cv2.LINE_AA)
    stk_x = []
    stk_y = []
    stk_x_p = []
    stk_y_p = []
    #global distance

    if len(faces) == 0:
        pass
    else:
        for i in range(0, len(faces)):
            x1 = faces[i][0]
            y1 = faces[i][1]
            x2 = faces[i][0] + faces[i][2]
            y2 = faces[i][1] + faces[i][3]

            mid_x = int((x1 + x2) / 2)
            mid_y = int((y1 + y2) / 2)
            
            stk_x += [mid_x]
            stk_y += [mid_y]
            stk_x_p += [mid_x]
            stk_y_p += [mid_y]
            
            pic = cv2.circle(pic, (mid_x, mid_y), 3, [255, 0, 0], -1)
            pic = cv2.rectangle(pic, (x1, y1), (x2, y2), [0, 255, 0], 2)

        if len(faces) == 2:
            distance = int(dist.euclidean((stk_x.pop(), stk_y.pop()), (stk_x.pop(), stk_y.pop())))
            pic = cv2.line(pic, (stk_x_p.pop(), stk_y_p.pop()),
                             (stk_x_p.pop(), stk_y_p.pop()), [0, 0, 255], 2)
        else:
            distance = 0

        if distance < 500 and distance != 0:
            pic = cv2.putText(pic, "Danger distance!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0, 255], 4)
            

        pic = cv2.putText(pic, str(distance / 10) + " cm", (300, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Detection Result', pic)
        if cv2.waitKey(100) == 27:
            break

cv2.destroyAllWindows()
