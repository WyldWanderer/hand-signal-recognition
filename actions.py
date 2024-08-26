import os

class Actions:
  #Trigger an action based on the gesture recognized
  def trigger_action(self, gesture, is_gesture_detected):
    if not is_gesture_detected:
      return
    match gesture:
      case "Fist":
        print(f"Triggering action for {gesture} gesture")
        os.system("open -a 'Google Chrome' https://www.google.com")
      case "Open":
        print(f"Triggering action for {gesture} gesture")
        #slack.pause_notifications()
      case "Thumbs Up":
        print("YAY")
      case "Pointing":
        print("My finger points")