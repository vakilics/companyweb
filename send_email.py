#Note: login to google account -> manage account -> security -> under 2-factor... -> create app password
import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "vakilitestmail@gmail.com"
password = "nrxbxbgeinzybxws"

receiver = "hamidgml@gmail.com"
context = ssl.create_default_context()
message = """
Hi!
This is the first test message from Vakili personal web app!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)