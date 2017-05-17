import RPi.GPIO as GPIO
import time
import picamera

buzzerPin = 17
ledPin = 23
sensorPin = 27
camera = picamera.PiCamera()

inputCounter = []

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sensorPin, GPIO.IN)

while True:
        openCounter = 0
        for c in range (0, 10):
                time.sleep(0.05)
                if GPIO.input(sensorPin):
                        openCounter += 1

        if openCounter > 3:
                GPIO.output(ledPin, GPIO.HIGH)
                print "OPEN"
                camera.capture('image1.jpg')
                break
        else:
                GPIO.output(ledPin, GPIO.LOW)
                print "CLOSED"
	
