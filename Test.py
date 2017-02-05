import time
from Button import Button
import CHIP_IO.GPIO as GPIO
import random
from Effects import FlashThru
from Effects import FlashAll

# tests

buttons = [
    Button("RED", "XIO-P0", "LCD-D4"),
    Button("YELLOW", "XIO-P1", "LCD-D6"),
    Button("BLUE", "XIO-P2", "LCD-D10"),
    Button("GREEN", "XIO-P3", "LCD-D12"),
    Button("WHITE", "XIO-P4", "LCD-D14")
]

scroll = FlashThru(buttons, 0.05, 0.01, 3)
blinkEm = FlashAll(buttons, 0.15, 0.15, 4)

def getRandomButton(btns):
    return btns[random.randint(0, len(buttons)-1)]

def getAnother(btns, current):
    btn = getRandomButton(btns)
    while btn == current:
        btn = getRandomButton(btns)
    return btn
print("millis: " + str(int(round(time.time() * 1000))))
btn = getRandomButton(buttons)

while True:
    btn = getAnother(buttons, btn)
    print(btn.color)
    btn.turnOn()
    while btn.isPressed() == False:
        time.sleep(0.05)  # sleep 50 milliseconds before checking again

    btn.turnOff()
    if random.randint(0, 1) == 0:
        scroll.run()
    else:
        blinkEm.run()
    time.sleep(0.25)  # sleep 50 milliseconds before checking again
