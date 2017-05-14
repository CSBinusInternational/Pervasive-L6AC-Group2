import RPi.GPIO as GPIO
import time

buzzerPin = 17
ledPin = 23
sensorPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(sensorPin, GPIO.IN)

door = 0

while True:
    if GPIO.input(sensorPin):
        GPIO.output(ledPin, GPIO.HIGH)
        print "OPEN"
    else:
        GPIO.output(ledPin, GPIO.LOW)
        print "CLOSED"
