
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
        times = range(self._timesRepeat)
        for i in times:
            for btn in self._buttons:
                btn.turnOn()
                time.sleep(self._onPer)
                btn.turnOff()
                time.sleep(self._delayTilNext)


# FlashAll takes an array of Button, the amount of seconds that all should be lighted (onAll), the amount of seconds
# delay until they light again, and the number of times that the entire row should be flashed.
class FlashAll():
    def __init__(self, buttons, onAll, delayTilNext, timesRepeat):
        self._buttons = buttons
        self._onPer = onAll
        self._delayTilNext = delayTilNext
        self._timesRepeat = timesRepeat

    def run(self):
        for i in range(self._timesRepeat):
            for btn in self._buttons:
                btn.turnOn()

            time.sleep(self._onPer)

            for btn in self._buttons:
                btn.turnOff()

            time.sleep(self._delayTilNext)

