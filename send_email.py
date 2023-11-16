import smtplib  # Standard lib to send emails. Lecture 218
import ssl


def send_email(message, user_email):
    host = 'smtp.gmail.com'
    port = 465

    username = 'martinoo1989@gmail.com'
    password = 'jkaetmbgxxmbzoqw'
    reciever = 'marcin.karbowniczyn@gmail.com'
    message = f"""\
Subject: New email from {user_email}
    
{message}
"""

    context = ssl.create_default_context()  # Nie wiem co to, mmogę później poszukać
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:  # Musimy dać "as" bo otwieramy funkcję która zwraca zmienną na której są metody
            server.login(username, password)
            server.sendmail(username, reciever, message)
    except Exception as e:
        print(e)
