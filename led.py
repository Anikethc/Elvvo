# This is the program that manages the LED.

# Imports
import RPi.GPIO as GPIO
import time

# Functions
def turnOnRedSingle():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT) # Red
    GPIO.setup(18, GPIO.OUT) # Yellow
    GPIO.setup(22, GPIO.OUT) # Green

    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(22, False)

def turnOffAll():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT) # Red
    GPIO.setup(18, GPIO.OUT) # Yellow
    GPIO.setup(22, GPIO.OUT) # Green

    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(22, False)

def turnOnRed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT) # Red
    GPIO.setup(18, GPIO.OUT) # Yellow
    GPIO.setup(22, GPIO.OUT) # Green

    redGPIO = GPIO.input(17)

    if redGPIO == True:
        GPIO.output(17, True)
    else:
        GPIO.output(22, False)
        time.sleep(0.5)
        GPIO.output(18, True)
        time.sleep(1)
        GPIO.output(18, False)
        time.sleep(0.5)
        GPIO.output(17, True)

def turnOnGreen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT) # Red
    GPIO.setup(18, GPIO.OUT) # Yello
    GPIO.setup(22, GPIO.OUT) # Green

    greenGPIO = GPIO.input(22)

    if greenGPIO == True:
        GPIO.output(22, True)
    else:
        GPIO.output(17, False)
        time.sleep(1)
        GPIO.output(22, True)