
# the following assums a normally-open pushbutton is connected between vcc and xio-p1
# sense once per second if the button is pressed (high) and output its state either
# 'pressed' or 'not-pressed'

import time
import CHIP_IO.GPIO as GPIO
GPIO.setup("XIO-P1", GPIO.IN)

isPressed = False
changed = False

while True:
    print( GPIO.input('XIO-P1'))
    time.sleep(1)
