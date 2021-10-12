import time
from email.message import EmailMessage
import smtplib, ssl
from core import defaults

class Timer:

    def __init__(self, name=None):
        self._start_time = None
        self.name = name
    
    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f'{self.name} | Elapsed time: {elapsed_time:0.4f} seconds')


def send_email(subject, message):
    port = defaults.EMAIL_SMTP_PORT
    smtp_server = defaults.EMAIL_SMTP
    sender = defaults.EMAIL_UID
    password = defaults.EMAIL_PWD
    recipient = ['ecms-file-transfers@arizonapipeline.com']

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(message)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print('Email Message Sent')
    except Exception as e:
        print(f'Email did not send: {e}')