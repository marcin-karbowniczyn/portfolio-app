import smtplib  # Standard lib to send emails. Lecture 218
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'martinoo1989@gmail.com'
password = 'jkaetmbgxxmbzoqw'
reciever = 'marcin.karbowniczyn@gmail.com'

# Backslash bez niczego kasuje \n
message = """\
Subject: New email from the Contact Me form
Hi!
How are you?

Bye!
"""

context = ssl.create_default_context()  # Nie wiem co to, mmogę później poszukać

try:
    with smtplib.SMTP_SSL(host, port, context=context) as server:  # Musimy dać "as" bo otwieramy funkcję która zwraca zmienną na której są metody
        server.login(username, password)
        server.sendmail(username, reciever, message)
except Exception as e:
    print(e)
