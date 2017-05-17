import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "diyhaliz@gmail.com"
toaddr = "adam.halim@yahoo.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your car..."
 
body = "Try send email no 2 from raspberry!!"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MYPASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
