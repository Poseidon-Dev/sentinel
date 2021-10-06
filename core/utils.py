import time
from email.message import EmailMessage
import smtplib, ssl
import core.config

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
    port = core.config.EMAIL_SMTP_PORT
    smtp_server = core.config.EMAIL_SMTP
    sender = core.config.EMAIL_UID
    password = core.config.EMAIL_PWD
    recipient = ['jwhitworth@arizonapipeline.com']

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