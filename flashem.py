
import time
from Button import Button
import CHIP_IO.GPIO as GPIO
import random

# simple test turns a single random button's LED on, turns it off for a quarter second then randomly selects another
# and on and on

buttons = [ # color, input pin (active low button), output pin (active low LED)
    Button("RED", "XIO-P0", "LCD-D4"),
    Button("YELLOW", "XIO-P1", "LCD-D6"),
    Button("BLUE", "XIO-P2", "LCD-D10"),
    Button("GREEN", "XIO-P3", "LCD-D12"),
    Button("WHITE", "XIO-P4", "LCD-D14")
]

isPressed = False


while True:
    btn = buttons[random.randint(0, len(buttons)-1)]
    print(btn.color)
    btn.turnOn()
    time.sleep(1)  # sleep 50 milliseconds before checking again
    btn.turnOff();
    time.sleep(0.25)  # sleep 50 milliseconds before checking again
#    for btn in buttons:
#        if btn.isLedOn():
#            if btn.isReleased():
#                btn.turnOff()
#                print(btn.color + " released")
#        else:
#            if btn.isPressed():
#                btn.turnOn()
#                print(btn.color + " pressed")
