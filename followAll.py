
# the following assumes that an LED is run from VCC to xio-p0 with its cathode in the latter
# ie: pulling pin low turns LED on, setting high turns it off

# it also assums a normally-open pushbutton is connected between ground and xio-p1
# when the pushbutton is pressed the LED should light. when it is released the
# LED should be extinguished

import time
from Button import Button
import CHIP_IO.GPIO as GPIO

buttons = [
    Button("RED", "LCD-D4", "LCD-D3"),
    Button("YELLOW", "LCD-D6", "LCD-D5"),
    Button("BLUE", "LCD-D10", "LCD-D7"),
    Button("GREEN", "LCD-D12", "LCD-D11"),
    Button("WHITE", "LCD-D14", "LCD-D13")
]

isPressed = False


while True:

    time.sleep(0.05)  # sleep 50 milliseconds before checking again

    for btn in buttons:
        if btn.isLedOn():
            if btn.isReleased():
                b.turnOff()
                print(btn.color + " released")
        else:
            if btn.isPressed():
                b.turnOn()
                print(btn.color + " pressed")
