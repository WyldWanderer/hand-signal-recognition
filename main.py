import cv2
import numpy as np
import os
import mediapipe as mp
import math

last_gesture_dectected = None
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def calculate_distance(point1, point2):
  return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def recognize_gesture(landmarks):
  global last_gesture_dectected

  palm_base = landmarks[0]
  thumb_tip = landmarks[4]
  index_tip = landmarks[8]
  middle_tip = landmarks[12]
  ring_tip = landmarks[16]
  pinky_tip = landmarks[20]

  thumb_index_distance = calculate_distance(thumb_tip, index_tip)
  index_middle_distance = calculate_distance(index_tip, middle_tip)
  middle_ring_distance = calculate_distance(middle_tip, ring_tip)
  ring_pinky_distance = calculate_distance(ring_tip, pinky_tip)

  if thumb_index_distance < 0.1 and index_middle_distance < 0.1 and middle_ring_distance < 0.1 and ring_pinky_distance < 0.1:
    gesture = "Fist"
  elif thumb_index_distance > 0.1 and index_middle_distance > 0.1 and middle_ring_distance > 0.1 and ring_pinky_distance > 0.1:
    gesture =  "Open"
  else:
    gesture = "Unknown"

  is_new_gesture_detected = gesture != last_gesture_dectected 
  last_gesture_dectected = gesture

  return gesture, is_new_gesture_detected
  
def trigger_action(gesture, is_gesture_detected):
  if not is_gesture_detected:
     return
  if gesture == "Fist":
    print("Triggering action for Fist gesture")
    os.system("open -a 'Google Chrome' https://www.google.com")
  elif gesture == "Open":
    print("Triggering action for Open gesture")
  else:
    print("Unknown gesture")

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
            gesture, is_gesture_detected = recognize_gesture(hand_landmarks.landmark)
            trigger_action(gesture, is_gesture_detected)
    else:
        last_gesture_dectected = None
    
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()