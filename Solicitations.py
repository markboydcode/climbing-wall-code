
import time

# milliseconds since the epoch
def currentMillis():
    int(round(time.time() * 1000)))

# Continuous takes a Button, the amount of seconds that it should solicit a press, and then turns on the LED for that
# amount of time waiting for its button to be pressed. If pressed before the time runs out, the solicit returns with
# a value of True. Otherwise, it returns when the time has elapsed and returns a value of False.
class Continuous():
    def __init__(self, btn, secondsOn):
        self._btn = btn
        self._secondsOn = secondsOn

    def solicit(self):
        startMillis = currentMillis()
        endMillis = self._secondsOn * 1000 + startMillis
        self._btn.turnOn()

        while currentMillis() < endMillis
            if btn.isPressed():
                return True

            time.sleep(0.25)  # sleep 25 milliseconds before checking again
        return False


def blinkTimes(durationMillis, times)
    # blink means off for half and on for half. Each of these halfs is a phase. There are twice as many phases as
    # there are flashes.
    phases = times * 2
    endMillis = currentMillis() + durationMillis

    phaseDuration = durationMillis / phases

    while currentMillis() < endMillis:
        if btn.isLedOn():
            btn.turnOff()
        else:
            btn.turnOn()
        endPhase = currentMillis() + phaseDuration

        while currentMillis() < endPhase
            if self._btn.isPressed():
                return True

            time.sleep(0.01)


# turns on for first third of time, flashes for next third, flashes twice the speed for last third
class TriPhase():
    def __init__(self, totalSeconds):


    def solicit(self, btn, totalSeconds):
        totalMillis = totalSeconds * 1000
        third = totalMillis / 3
        end1st = currentMillis() + third
        btn.turnOn()

        while currentMillis() < end1st:
            if self._btn.isPressed():
                return True
            time.sleep(0.01)

        perssed = blinkTimes(third, 2);
        if (pressed)
            return True

        return blinkTimes(third, 6);
