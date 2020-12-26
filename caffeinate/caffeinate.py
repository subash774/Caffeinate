from threading import Thread
from pynput.keyboard import Key, Controller, Listener
import argparse
import time
from threading import Thread
from datetime import datetime


hist = 0
last_online = datetime.now()

keyboard = Controller()


def on_press(key):
    pass


def on_release(key):
    global hist
    
    if key == Key.esc:
        hist += 1

        # if esc pressed 3 times, exit
        if hist == 3:
        # Stop listener
            return False
    else:
        hist = 0


def stay_awake(wait):
    global last_online
    print(f"Serving caffeine every {wait} seconds")
    while hist < 3:
        if (datetime.now() - last_online).seconds > wait:
            keyboard.press(Key.shift)
            keyboard.release(Key.shift)
            last_online = datetime.now()
        time.sleep(1)
    return False


def run():
    """
    Listens for user's keystrokes, if none for given time, shift is pressed to keep the computer awake
    Args:
        --time ([int]): [default time interval for keypress to take place]
    """
    wait = 90
    try:
        parser=argparse.ArgumentParser()
        parser.add_argument('--time', help='Activate after certain time in seconds')
        args=parser.parse_args()
        wait = int(args.time)

    except Exception as e:
        print(f"No time argument passed, serving caffeine every {wait} secs")
        pass

    listener = Listener(
        on_press=on_press,
        on_release=on_release)
    awake = Thread(target=stay_awake, args=(wait,))

    listener.start()
    awake.start()
    listener.join()
    awake.join()
