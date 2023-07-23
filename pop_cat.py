from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller as C
import time

mouse = Controller()
keyboard = C()
delay=0.18
try:
    def show_desktop():
        """presses the key combination win+D to minimise all apps."""
        time.sleep(1.8)
        keyboard.press(Key.cmd)
        time.sleep(0.18)
        keyboard.press('d')
        time.sleep(0.18)
        keyboard.release(Key.cmd)
        keyboard.release('d')

    def sleep(delay):
        """Pauses the execution for delay seconds."""
        time.sleep(delay)

    sleep(delay)
    show_desktop()
    sleep(delay+1.8)

    # Step 1: to open Microsoft Edge
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    sleep(delay)
    keyboard.type("Microsoft Edge") # <--- You can change the browser here.
    sleep(delay)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(delay+2.7)

    # step 2 : open the new tab in the browser
    keyboard.press(Key.ctrl)
    sleep(delay)
    keyboard.press('t')
    keyboard.release(Key.ctrl)
    keyboard.release('t')

    # step 3 : Maximise the window
    # we can maximise by the following methods: alt + space & tab 5 times then enter, or we can use win + uparrow, which is much better.
    sleep(delay)
    keyboard.press(Key.cmd)
    sleep(delay)
    keyboard.press(Key.up)
    keyboard.release(Key.cmd)
    keyboard.release(Key.up)
    sleep(delay)


    # Step: 4 search for the website popcat.click in the search bar.
    keyboard.type("https://popcat.click/")
    sleep(delay)
    keyboard.press(Key.enter)
    sleep(delay)
    keyboard.release(Key.enter)
    sleep(delay+1.8)
    
    # Step 5: moved to the center of the screen once the website loads...at coordinates: (855, 428)
    # Note: coordinate (0,0) is the top left corner of the screen.
    mouse.position = (855, 428) # coordinates to center of PC screen (here laptop screen  is used)
    # Coordinates click till the coordinate is not (0,0)
    while mouse.position != (0,0):
        """To terminate the program...move the mouse pointer to top left part of the screen i.e at the co-ordinate (0, 0)"""
        time.sleep(delay-0.1)
        mouse.press(Button.left)
        time.sleep(delay-0.1)
        mouse.release(Button.left)
    
except:
    exit()