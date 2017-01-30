
import CHIP_IO.GPIO as GPIO

class Button():
    def __init__(self, color, inputPin, outputPin):
        self.__color = color
        self.__outputPin = outputPin
        self.__inputPin = inputPin

        GPIO.setup(outputPin, GPIO.OUT)
        GPIO.setup(inputPin, GPIO.IN)
        GPIO.output(outputPin, GPIO.HIGH) # turn LED off (active low common cathode form)


    @property
    def color(self):
        return self.__color

    def isPressed(self):
        return GPIO.input(self.__inputPin) == 0 # button is active low since it pins have pull-up resistors

    def isReleased(self):
        return GPIO.input(self.__inputPin) == 1 # button is active low, releasing button lets pull-up resistors pull high

    def turnOn(self):
        GPIO.output(self.__outputPin, GPIO.LOW) # turn LED on via active low (ie: sink) common cathode pin

    def turnOff(self):
        GPIO.output(self.__outputPin, GPIO.HIGH) # turn LED off via driving high


