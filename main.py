#Necessary imports to run the code, 
import cv2
import mediapipe as mp
from integrations.slack_actions import SlackManager
from gestures import Gestures
from actions import Actions

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
slack = SlackManager()
gestures = Gestures()
actions = Actions()

#Main loop to capture the video feed from the camera, should open a window with the hand tracking as well
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
            gesture, is_gesture_detected = gestures.recognize_gesture(hand_landmarks.landmark)
            actions.trigger_action(gesture, is_gesture_detected)
    else:
        last_gesture_dectected = None
    #If you would prefer to not see the hand tracking window, comment out the line below
    cv2.imshow('Hand Tracking', image)
    #stops the video feed if the escape key is pressed
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()