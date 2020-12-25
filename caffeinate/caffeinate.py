from threading import Thread
from pynput.keyboard import Key, Controller, Listener
import argparse
import time
from threading import Thread
from datetime import date, datetime


hist = []
last_online = datetime.now()

keyboard = Controller()


def on_press(key):
    pass

def on_release(key):
    print('{0} release'.format(
        key))
    global hist
    
    if key == Key.esc:
        hist.append(True)

        # if esc pressed 3 times, exit
        if len(hist) == 3:
        # Stop listener
            return False
    else:
        hist = []


def stay_awake(wait):
    global last_online
    print(f"Serving caffeine every {wait} seconds")
    while len(hist) < 3:
        if (datetime.now() - last_online).seconds > wait:
            x = last_online - datetime.now()
            keyboard.press(Key.shift)
            keyboard.release(Key.shift)
            last_online = datetime.now()
        time.sleep(1)
    return False


def run():
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
