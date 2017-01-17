
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

import time
import CHIP_IO.GPIO as GPIO
GPIO.setup("XIO-P0", GPIO.OUT)

GPIO.output("XIO-P0", GPIO.HIGH)

while True:
    GPIO.output("XIO-P0", GPIO.LOW)
    time.sleep(1)
    GPIO.output("XIO-P0", GPIO.HIGH)
    time.sleep(1)
