# -*- coding: utf-8 -*-
"""CupObjectrondetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ClaudioCazzetta/VISIONE-E-PERCEZIONE/blob/Rox/TutorialObjectron.ipynb

# Tutorial multimediale Objectron Mediapipe

---
*Cazzetta Claudio e Valanzano Rocchina*

Installazione mediapipe
"""

#!pip install opencv-python mediapipe

"""import Github project"""

#!git clone https://github.com/ClaudioCazzetta/VISIONE-E-PERCEZIONE.git

"""import delle dipendenze"""

import cv2
import mediapipe as mp
#from google.colab.patches import cv2_imshow
import os

"""Setup di mediapipe"""

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

"""Link utili per le immagini disponibili

Immagine1: "/content/VISIONE-E-PERCEZIONE/media/tazza1.jpg"

Immagine1: "/content/VISIONE-E-PERCEZIONE/media/tazza3.jpg"

Immagine1: "/content/VISIONE-E-PERCEZIONE/media/tazza6.jpg"

Immagine2: "/content/VISIONE-E-PERCEZIONE/media/tazza7.jpg"

Detection e tracciamento immagini 2D
"""

with mp_objectron.Objectron(static_image_mode=True,
                            max_num_objects=1,
                            min_detection_confidence=0.5,
                            model_name='Cup') as objectron:
  	
    #image = cv2.imread("/home/rox/Scrivania/Progetto/tazza7.jpg")
    image = cv2.imread("/home/rox/Scrivania/original/catkin_ws/src/img_cloud_point/Capture.jpg");
    cv2.imshow('',image)
    cv2.waitKey(1000)

      
    # Conversione dell'immagine BGR a RGB e processamento con MediaPipe Objectron.
    #results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imshow('',image)
    cv2.waitKey(1000)
    results = objectron.process(image)
 
    # Disegnare landmarks della box.
    annotated_image = image.copy()
    for detected_object in results.detected_objects:
      mp_drawing.draw_landmarks(
          annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
      mp_drawing.draw_axis(annotated_image, detected_object.rotation,
                           detected_object.translation)      
      os.chdir("/home/rox/Scrivania/original/catkin_ws/src/img_cloud_point/")
      cv2.imwrite('annotated_image' + '.jpg', annotated_image)
      print('File generato')
      cv2.imshow("annotated",annotated_image)
      cv2.waitKey(3000)

"""Detection e tracciamento video"""


"""

video = "/content/VISIONE-E-PERCEZIONE/media/video1.mp4";
cap = cv2.VideoCapture(video)
f = 20;
cap.set(1, f)

with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=1,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.80,
                            model_name='Cup') as objectron:
  while cap.isOpened():
    cap.set(1, f)
    f = f + 20;
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
        # Se carichi un video, usa 'break' invece di 'continue'.
      break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = objectron.process(image)

    # Disegnare landmarks della box.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(
              image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(image, detected_object.rotation,
                                 detected_object.translation)
    # Flip the image horizontally for a selfie-view display.
    #cv2_imshow( cv2.flip(image, 1))
    cv2_imshow(image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()

"""
