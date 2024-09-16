# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:52:08 2021

@author: gmunaretti
"""

fromaddr = "n@intercargo.com.ar"
password = "pe"
toaddr = "g@intercargo.com.ar"

import smtplib


server = smtplib.SMTP('correo.intercargo.com.ar', 587)
server.starttls()
server.login(fromaddr,password)
mensaje = "Hola Mundo SMTP"
server.sendmail(fromaddr, toaddr,mensaje)
server.quit()

