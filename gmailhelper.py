import string
import smtplib
import time
import imaplib
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('gmailhelper.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_last_gmail_from_label(gmail_label):
    try:
        mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        mail.login(config.FROM_EMAIL,config.FROM_PWD)
        mail.select(gmail_label)
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        latest_email_id = int(len(id_list))
        type, data = mail.fetch(latest_email_id, '(RFC822)' )
        return data
    except Exception, e:
        logger.error(str(e))

def get_mail_subject(full_email):
    for response_part in full_email:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            email_subject = msg['subject']
            return email_subject

def get_mail_from_mail(full_email):
    for response_part in full_email:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            email_from_elements = msg['from'].split()
            return str.translate(email_from_elements[len(email_from_elements)-1],None,"<>")

def send_gmail(subject,body):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.FROM_EMAIL
        msg['To'] = config.TO_EMAIL
        msg['Subject'] = str(subject)
        body = body
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(config.SMTP_SERVER,config.SMTP_PORT)
        server.starttls()
        server.login(config.FROM_EMAIL, config.FROM_PWD)
        text = msg.as_string()
        server.sendmail(config.FROM_EMAIL, config.TO_EMAIL, text)
        server.quit()
    except Exception, e:
        logger.error(str(e))

def main():
    last_mail = get_last_gmail_from_label(GMAIL_LABEL_TARGET_TEMPERATURE)
    logger.info(get_mail_from_mail(last_mail))


if __name__ == "__main__":
    main()
