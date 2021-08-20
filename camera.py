# opencv file to load the video, 

import cv2
from model import FacialExpressionModel
import numpy as np

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')         # to get facial expression detection 
model = FacialExpressionModel("model.json", "model_weights.h5")              # load the config for the model and save the model weights
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):                     # initialoization of videocapture function
    def __init__(self):
        self.video = cv2.VideoCapture('/home/rhyme/Desktop/Project/videos/facial_exp.mkv') 
# above code to get the videocapture attribute that takes actual vidoe path,or  0 for webcam of laptop, 1 for first camera connected on laptop. 

    def __del__(self):
        self.video.release()      # now we relase the capture device after getting the frames from the video.

    # returns camera frames along with bounding boxes and predictions
    
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)         # load the video and take a look at each frame it should in gray scale
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w] 

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis]) # now going to predict face emotion for that we are using openCV

            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)             # then use a openCV face detector to create a runding boxes aroud the each frame. and put the text that is predicted by the opencv

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()
