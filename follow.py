
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between vcc and xio-p1
# when the pushbutton is pressed the LED should light. when it is released the
# LED should be extinguished

import time
import CHIP_IO.GPIO as GPIO
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.IN)

GPIO.output("XIO-P0", GPIO.HIGH) # turn LED off

while True:
    if GPIO.input('XIO-P1') :
        GPIO.output("XIO-P0", GPIO.LOW)
    else
        GPIO.output("XIO-P0", GPIO.HIGH)
    time.sleep(0.05)  # sleep 50 milliseconds before checking again
