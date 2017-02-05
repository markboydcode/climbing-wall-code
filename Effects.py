
import range
import time

# FlashThru takes an array of Button, the amount of seconds that each should be lighted (onPer), the amount of seconds
# delay until the next button in the array is lighted, and the number of times that the row should be flashed.
class FlashThru():
    def __init__(self, buttons, onPer, delayTilNext, timesRepeat):
        self._buttons = buttons
        self._onPer = onPer
        self._delayTilNext = delayTilNext
        self._timesRepeat = timesRepeat

    def run(self):
        for i in range(self._timesRepeat - 1):
            for btn in self._buttons:
                btn.turnOn()
                time.sleep(self._onPer)
                btn.turnOff()
                time.sleep(self._delayTilNext)
