
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between ground and xio-p1

# the program randomly lights the LED. if the button is pushed within 2 seconds the LED
# is put out and a new random delay from 1 to 4 seconds will ensue before the LED is lit
# again.

# if the LED is not pressed within two seconds then
# it blinks at two times per second until the button is pressed and
# held for 3 seconds to reset it. it will then turn turn on solid for one second, turn off,
# then resume turning on in a random number of seconds between one and four.

import time
import CHIP_IO.GPIO as GPIO

def newButton(ledOutput, buttonInput):
    GPIO.setup(ledOutput, GPIO.OUT)
    GPIO.setup(buttonInput, GPIO.IN)
    return {
        "led": ledOutput,
        "btn": buttonInput
    }

buttons = [
    newButton("LCD-D4", "LCD-D3")
]


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
