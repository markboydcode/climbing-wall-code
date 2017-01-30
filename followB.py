
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between ground and xio-p1
# when the pushbutton is pressed the LED should light. when it is released the
# LED should be extinguished

import time
import Button
import CHIP_IO.GPIO as GPIO

b = Button("XIO-P1", "XIO-P0")
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.IN)

isPressed = False


while True:
    if isPressed:
        if b.isReleased()
            isPressed = False
            b.turnOff()
            print("released")
    else:
        if b.isPressed()
            isPressed = True
            b.turnOff()
            print("pressed")
    time.sleep(0.05)  # sleep 50 milliseconds before checking again
