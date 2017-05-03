import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzerNum = 17
sensorNum = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensorNum, GPIO.IN)

while True:
    if GPIO.input(sensorNum):
        print("Detected")
    else 
    time.sleep(2)

GPIO.cleanup()
