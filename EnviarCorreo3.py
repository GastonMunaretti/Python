# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:06:12 2021

@author: gmunaretti
"""

SERVER = "c.intercargo.com.ar"
FROM = "n@intercargo.com.ar"
TO = ["g@intercargo.com.ar"] # must be a list

SUBJECT = "Hello!"
TEXT = "This is a test of emailing through smtp of example.com."

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login("n@intercargo.com.ar", "p")
server.sendmail(FROM, TO, message)
server.quit()