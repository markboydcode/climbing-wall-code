
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

    time.sleep(3.00)  # sleep 50 milliseconds before checking again
    print("----------------------"
    for btn in buttons:
        print("checking: " + btn.color + " - on: " + btn.isLedOn())
        if btn.isLedOn():
            btn.turnOff()
            #if btn.isReleased():
            #    btn.turnOff()
            #    print(btn.color + " released")
        else:
            btn.turnOn()
            #if btn.isPressed():
            #    btn.turnOn()
            #    print(btn.color + " pressed")
