import smtplib  # Standard lib to send emails. Lecture 218
import ssl
import os

from dotenv import load_dotenv

load_dotenv()


def send_email(message, user_email):
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    username = os.getenv('USERNAME_GMAIL')

    # Ta zmienna jest zapisana za pomocą "Edytu zmienne środowiskowe" a nie w pliku .env
    password = os.getenv('PASSWORD_GMAIL')

    reciever = 'marcin.karbowniczyn@gmail.com'
    message = f"""\
Subject: New email from {user_email}

From: {user_email}   
{message}
"""

    context = ssl.create_default_context()  # Nie wiem co to, mogę później poszukać
    with smtplib.SMTP_SSL(host, port, context=context) as server:  # Musimy dać "as" bo otwieramy funkcję która zwraca zmienną na której są metody
        server.login(username, password)
        server.sendmail(username, reciever, message)
