import time
from pynput import mouse

mouse_controller = mouse.Controller()

def on_scroll(x, y, dx, dy):
    print(dx, 'dx', dy, 'dy')
    try:
        stop_listening()
        print('doubling')
        mouse_controller.scroll(3 * dx, 3 * dy)
    finally:
        start_listening()

listener = None

def start_listening():
    global listener

    if listener:
        return
    listener = mouse.Listener(on_scroll=on_scroll, suppress=False)
    listener.start()


def stop_listening():
    global listener

    if listener:
        listener.stop()
    listener = None


start_listening()

while True:
    time.sleep(30)
