import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
pinNum = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinNum, GPIO.OUT)
GPIO.output(pinNum, True)
time.sleep(0.3)
GPIO.output(pinNum, False)

GPIO.cleanup()
