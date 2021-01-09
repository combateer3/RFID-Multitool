import smtplib
import json


def get_creds():
    with open('creds.json') as f:
        return json.load(f)


def create_email(subject, body):
    return f'Subject: {subject}\n\n{body}'


def send_email(to, msg):
    creds = get_creds()
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(creds['email_address'], creds['password'])
        smtp.sendmail(creds['email_address'], to, msg)
        smtp.quit()

