# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

subject='Email subject'
html = """\
<html>
  <head></head>
  <body>
    <p><b>Hi!</b><br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""


class SendEmail:
    def __init__(self, fromx, password, to, subject, html):
        msg = MIMEMultipart()
        # create and start mail server
        server = smtplib.SMTP('smtp-mail.outlook.com: 587')      
        server.starttls()
        # Login Credentials for sending the mail
        msg['From']='Raspberry PI <{}>'.format(fromx)
        msg['To']=to
        msg['Subject'] =subject
        password=password
        server.login(fromx,  password)
        msg.attach(MIMEText(html,  'html'))       
        # send the message via the server.
        server.sendmail(msg['From'],  msg['To'],  msg.as_string())
        server.quit()
                 
SendEmail(sys.argv[1], sys.argv[2], sys.argv[3], subject,  html)
