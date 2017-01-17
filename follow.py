
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between ground and xio-p1
# when the pushbutton is pressed the LED should light. when it is released the
# LED should be extinguished

import time
import CHIP_IO.GPIO as GPIO
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.IN)

GPIO.output("XIO-P0", GPIO.HIGH) # turn LED off
isPressed = False


while True:
    if isPressed:
        if GPIO.input('XIO-P1') == 1 : # button was released since it has a pull-up resistor
            isPressed = False
            GPIO.output("XIO-P0", GPIO.HIGH) # turn LED off
            print("released")
    else:
        if GPIO.input('XIO-P1') == 0 : # button was pressed since button pulls it low
            isPressed = True
            GPIO.output("XIO-P0", GPIO.LOW) # turn LED on
            print("pressed")
    time.sleep(0.05)  # sleep 50 milliseconds before checking again
