import smtplib
import ssl
import os

from dotenv import load_dotenv

load_dotenv()


def send_email(message, user_email):
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    username = os.getenv('USERNAME_GMAIL')
    password = os.getenv('PASSWORD_GMAIL')

    reciever = 'marcin.karbowniczyn@gmail.com'
    message = f"""\
Subject: New email from {user_email}

From: {user_email}   
{message}
"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
