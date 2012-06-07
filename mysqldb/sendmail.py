#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.MIMEText import MIMEText

def send_email(message, to_addr):
	msg = MIMEText(message)
	msg['Subject'] = "Omu Kampus Kart Geçici Şifreniz"
	msg['From'] = 'omukampuskart@gmail.com'
	msg['To'] = to_addr
	server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('omukampuskart@gmail.com', 'omukampuskart')
	server.sendmail('omukampuskart@gmail.com', to_addr, msg.as_string())
	server.close()
