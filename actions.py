import mail

import socket
import json


def test_message():
    print("This is a test!")


def rpi_ip_addr():
    # fetch local IP address
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname + '.local')

    with open('creds.json') as f:
        creds = json.load(f)
        to = creds['cell_email']

    # create and send message
    msg = mail.create_email('RPi IP Address', ip_addr)
    mail.send_email(to, msg)

