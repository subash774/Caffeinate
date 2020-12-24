from pynput.keyboard import Key, Controller
import time


def stay_awake():
    keyboard = Controller()
    while True:
        print("Serving caffeine...press any key to stop")
        time.sleep(5)
        keyboard.press(Key.shift)
        keyboard.release(Key.shift)

if __name__ == "__main__":
    stay_awake()