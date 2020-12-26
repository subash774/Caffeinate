import argparse
import time
from datetime import datetime
from threading import Thread
from pynput.keyboard import Key, Controller, Listener


class Caffeinate:

    def __init__(self):
        self.hist = 0
        self.last_online = datetime.now()
        self.keyboard = Controller()

    def on_press(self, key):
        pass

    def on_release(self, key):
        if key == Key.esc:
            self.hist += 1

            # if esc pressed 3 times, exit
            if self.hist == 3:
                # Stop listener
                return False
        else:
            self.hist = 0

    def stay_awake(self, wait):
        print(f"Serving caffeine every {wait} seconds")
        while self.hist < 3:
            if (datetime.now() - self.last_online).seconds > wait:
                self.keyboard.press(Key.shift)
                self.keyboard.release(Key.shift)
                self.last_online = datetime.now()
            time.sleep(1)
        return False


def run():
    """
    Listens for user's keystrokes, if none for given time, shift is pressed to keep the computer awake
    Args:
        --time ([int]): [default time interval for keypress to take place]
    """

    caffeinate = Caffeinate()
    parser = argparse.ArgumentParser()
    parser.add_argument('--time', type=int, default=90, help='Activate after certain time in seconds')
    args = parser.parse_args()

    listener = Listener(
        on_press=caffeinate.on_press,
        on_release=caffeinate.on_release)
    awake = Thread(target=caffeinate.stay_awake, args=(args.time,))

    listener.start()
    awake.start()
    listener.join()
    awake.join()


if __name__ == '__main__':
    run()
