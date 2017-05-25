# GPIO imports
import RPi.GPIO as GPIO
import time
import picamera

# email imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# declare pin nums
buzzerPin = 17
sensorPin = 27
camera = picamera.PiCamera()
camera.rotation = 180

# set pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# initialize pins
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(sensorPin, GPIO.IN)

# loop until stop
while True:
        if GPIO.input(sensorPin):
                time.sleep(0.5)
                GPIO.output(buzzerPin, GPIO.LOW)
                camera.capture('image.jpg')
                print "OPEN"
                break
        else:
                GPIO.output(buzzerPin, GPIO.HIGH)
                print "CLOSED"
				
time.sleep(3)
GPIO.output(buzzerPin, GPIO.HIGH)
	
GPIO.cleanup()

# send email with image attached
fromaddr = "diyhaliz@gmail.com"
toaddr = "claudiayhaliz@yahoo.com"

# create container for the message
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Pervasive Alarm Security System Notification"
 
body = "Please see the attached image. (This is sent from Raspberry.)"
 
msg.attach(MIMEText(body, 'plain'))

# set image and attach
filename = "image.jpg"
attachment = open("/home/pi/Downloads/image.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

# login to sender's email acc and send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MYPASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
