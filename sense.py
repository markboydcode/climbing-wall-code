
# the following assums a normally-open pushbutton is connected between to xio-p1
# if its other lead is connected to vcc this program always outputs 1's. If it is
# connected to ground it outputs 1 when not pressed, and 0 when pressed. this tells
# us that the pin has a pull-up resistor which means we need to pull it low to signal
# some outside event like pushing a button.

import time
import CHIP_IO.GPIO as GPIO
GPIO.setup("XIO-P1", GPIO.IN)

isPressed = False
changed = False

while True:
    print( GPIO.input('XIO-P1'))
    time.sleep(1)
