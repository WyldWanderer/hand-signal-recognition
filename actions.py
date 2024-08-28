import os
from integrations.system_actions import SystemActions;
from integrations.slack_actions import SlackManager

system_actions = SystemActions()
slack = SlackManager()

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
        system_actions.toggle_do_not_disturb()
      case "Thumbs Up":
        print(f"Triggering action for {gesture} gesture")
      case "Pointing":
        print("My finger points")