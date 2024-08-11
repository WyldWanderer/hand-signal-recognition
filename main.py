import cv2
import numpy as np
import os
import mediapipe as mp
import math


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def calculate_distance(point1, point2):
  return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

#def recognize_gesture(landmarks):
    

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    
    
    image_rgb = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()