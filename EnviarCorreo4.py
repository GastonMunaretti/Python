# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:13:24 2021

@author: gmunaretti
"""


from email.mime.text import MIMEText
from smtplib import SMTP



def main():
    from_address = "n@intercargo.com.ar"
    to_address = "g@intercargo.com.ar"
    message = "Hello, world!"
    
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
    
    smtp = SMTP("c.intercargo.com.ar:587")
    smtp.login(from_address, "p")
    
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
if __name__ == "__main__":
    main()