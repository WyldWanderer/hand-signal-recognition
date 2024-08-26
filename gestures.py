import math

class Gestures:
    def __init__(self):
        self.last_gesture_dectected = None

    def calculate_distance(self, point1, point2):
      return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    def recognize_gesture(self, landmarks):
      global last_gesture_dectected
      #Get the landmarks for the hand
      palm_base = landmarks[0]
      thumb_tip = landmarks[4]
      index_tip = landmarks[8]
      middle_tip = landmarks[12]
      ring_tip = landmarks[16]
      pinky_tip = landmarks[20]

      thumb_index_distance = self.calculate_distance(thumb_tip, index_tip)
      index_middle_distance = self.calculate_distance(index_tip, middle_tip)
      middle_ring_distance = self.calculate_distance(middle_tip, ring_tip)
      ring_pinky_distance = self.calculate_distance(ring_tip, pinky_tip)

      thumb_palm_distance = self.calculate_distance(thumb_tip, palm_base)
      index_palm_distance = self.calculate_distance(index_tip, palm_base)
      middle_palm_distance = self.calculate_distance(middle_tip, palm_base)
      ring_palm_distance = self.calculate_distance(ring_tip, palm_base)
      pinky_palm_distance = self.calculate_distance(pinky_tip, palm_base)

      #Calculate the distance between different hand landmarks to recognize the gesture
      if thumb_palm_distance < 0.3 and index_palm_distance < 0.3 and middle_palm_distance < 0.3 and ring_palm_distance < 0.3 and pinky_palm_distance < 0.3:
        gesture = "Fist"
      elif thumb_palm_distance > 0.3 and index_palm_distance > 0.5 and middle_palm_distance > 0.5 and ring_palm_distance > 0.5 and pinky_palm_distance > 0.5:
        gesture = "Open"
      elif thumb_palm_distance > 0.3 and index_palm_distance < 0.3 and middle_palm_distance < 0.3 and ring_palm_distance < 0.3 and pinky_palm_distance < 0.3:
        gesture = "Thumbs Up"
      elif thumb_palm_distance < 0.3 and index_palm_distance > 0.5 and middle_palm_distance < 0.3 and ring_palm_distance < 0.3 and pinky_palm_distance < 0.3:
        gesture = "Pointing"
      else:
        gesture = "Unknown"

      is_new_gesture_detected = gesture != self.last_gesture_dectected 
      self.last_gesture_dectected = gesture

      return gesture, is_new_gesture_detected
    
    

