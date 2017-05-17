import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "diyhaliz@gmail.com"
toaddr = "adam.halim@yahoo.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your car... (With attachment)"
 
body = "Please see the attached image. (This is sent from Raspberry.)"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "cat.jpg"
attachment = open("/home/pi/Pictures/cat.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MYPASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
