# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:58:39 2021

@author: gmunaretti
"""

#==============================================================================
#=  FUNCIONA CORRECTAMENTE                                                    =
#==============================================================================



import smtplib 
from email.message import EmailMessage 

email_subject = "Email test from Python" 
sender_email_address = "n@intercargo.com.ar" 
receiver_email_address = "p@intercargo.com.ar" 
email_smtp = "correo.intercargo.com.ar" 
email_password = "peperoni" 

# Create an email message object 
message = EmailMessage() 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 

# Set email body text 
message.set_content("Pablo, seguro te la comes!") 

# Set smtp server and port 
server = smtplib.SMTP(email_smtp, '587') 

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls() 

# Login to email account 
server.login(sender_email_address, email_password) 

# Send email 
server.send_message(message) 

# Close connection to server 
server.quit()



