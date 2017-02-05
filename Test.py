import time
from Button import Button
import CHIP_IO.GPIO as GPIO
import random
from Effects import FlashThru

# tests

buttons = [
    Button("RED", "XIO-P0", "LCD-D4"),
    Button("YELLOW", "XIO-P1", "LCD-D6"),
    Button("BLUE", "XIO-P2", "LCD-D10"),
    Button("GREEN", "XIO-P3", "LCD-D12"),
    Button("WHITE", "XIO-P4", "LCD-D14")
]

scroll = FlashThru(buttons, 0.3, 0.1, 3)

while True:
    btn = buttons[random.randint(0, len(buttons)-1)]
    print(btn.color)
    btn.turnOn()
    while btn.isPressed() == False:
        time.sleep(0.05)  # sleep 50 milliseconds before checking again

    btn.turnOff()
    scroll.run()
    time.sleep(0.25)  # sleep 50 milliseconds before checking again
