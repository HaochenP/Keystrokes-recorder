import keyboard
from datetime import datetime
import sys


class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def start(self):
        keyboard_events = None  # List of keys recorded
        while True:
            if keyboard_events is None:  # Start of the program where no keys are recorded
                self.start_dt = datetime.now()
                keyboard.wait('/')  # Start recording keystrokes
                print(f"{datetime.now()} - Started keylogger")
                keyboard.start_recording()  # Keys recorded
                keyboard.wait("/")  # Stop recording keystrokes
                print("stop")
                keyboard_events = keyboard.stop_recording()  # Stores all the key presses
                print(keyboard_events)
                keyboard_events = keyboard_events[:-1]  # Exclude the trigger key
            else:
                while keyboard_events is not None:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_DOWN and event.name == '.':
                        keyboard_events = None  # Re-record keystrokes
                        print("Record again")
                    elif event.event_type == keyboard.KEY_DOWN and event.name == '/':
                        keyboard.play(keyboard_events, speed_factor=1)  # Replay the recorded keys
                        print("Repeated")
                    elif event.event_type == keyboard.KEY_DOWN and event.name == ',':
                        print("END")  # End program
                        sys.exit()


if __name__ == "__main__":
    keylogger = Keylogger(interval=10)
    keylogger.start()


