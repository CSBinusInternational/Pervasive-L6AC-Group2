import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzerPin = 17
ledPin = 23
sensorPin

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)

while True:
	if :
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(10)
		GPIO.output(ledPin, GPIO.LOW)