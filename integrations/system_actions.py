import subprocess

class SystemActions:

  @staticmethod
  def toggle_do_not_disturb():
    applescript = '''
    tell application "System Events"
      tell process "Control Center"
        click menu bar item "Control Center" of menu bar 1
        click button "Focus" of group 1 of window "Control Center"
        click button "Do Not Disturb" of window "Control Center"
      end tell
    end tell
    '''
    
    try:
      subprocess.run(["osascript", "-e", applescript], check=True)
      print("Do Not Disturb toggled")
    except subprocess.CalledProcessError as e:
      print(f"Error toggling Do Not Disturb: {e}")