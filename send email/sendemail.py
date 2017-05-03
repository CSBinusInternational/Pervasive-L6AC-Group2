import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("diyhaliz@gmail.com", "MYPASSWORD")
 
msg = "Test python no 1 raspberry"
server.sendmail("diyhaliz@gmail.com", "adam.halim@yahoo.com", msg)
server.quit()
