import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = "name"
email['to'] ='email'
email['subject'] = "Test python email"

email.set_content(html.substitute({'name':'Tin Tin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email.com','password')
    smtp.send_message(email)
    print('all works .. !')