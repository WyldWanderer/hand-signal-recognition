import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackManager:
  def __init__(self):
    load_dotenv()
    self.slack_token = os.getenv("SLACK_TOKEN")
    self.client = WebClient(token=os.getenv("SLACK_BOT"))
                            
  def pause_notifications(self, duration_minutes=60):
    try:
      response = self.client.dnd_setSnooze(num_minutes=duration_minutes)
      if response["ok"]:
        print(f"Notifications paused for {duration_minutes} minutes")
        return True
      else:
        print("Error pausing notifications")
        return False

    except SlackApiError as e:
      print(f"Error pausing notifications: {e.response['error']}")
      return False