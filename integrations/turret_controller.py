import serial
import time

class IRTurretController:

  def send_command(command):
    commands = {
      'left': '8',
      'right': '5A',
      'up': '18',
      'down': '52',
      'ok': '1C',
      'cmd1': '45',
      'cmd2':'46',
      'cmd3': '47',
      'cmd4': '44',
      'cmd5': '40',
      'cmd6': '43',
      'cmd7': '7',
      'cmd8': '15',
      'cmd9': '9',
      'cmd0': '19',
      'star': '16',
      'hashtag': 'D',
    }

    ser = serial.Serial('/dev/cu.usbmodemflip_Umiporio1', 9600)
    time.sleep(2)  # Wait for connection
    ser.write(f'ir tx NEC 00 {commands[command]}\r\n'.encode())
    ser.close()

IR_Turret_Controller.send_command("cmd1")


