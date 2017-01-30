# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between ground and xio-p1
# when the pushbutton is pressed the LED should light. when it is released the
# LED should be extinguished

import time
from Button import Button
import CHIP_IO.GPIO as GPIO

buttons = [
    Button("RED", "XIO-P0", "LCD-D4"),
    Button("YELLOW", "XIO-P1", "LCD-D6"),
    Button("BLUE", "XIO-P2", "LCD-D10"),
    Button("GREEN", "XIO-P3", "LCD-D12"),
    Button("WHITE", "XIO-P4", "LCD-D14")
]

isPressed = False


while True:

    time.sleep(0.05)  # sleep 50 milliseconds before checking again
    for btn in buttons:
        print("checking: " + btn.color + " - on: " + str(btn.isLedOn()) + ", pressed: " + str(btn.isPressed()) + ", released: " + str(btn.isReleased()))
        if btn.isLedOn():
            if btn.isReleased():
                btn.turnOff()
                print(btn.color + " released")
        else:
            if btn.isPressed():
                btn.turnOn()
                print(btn.color + " pressed")
