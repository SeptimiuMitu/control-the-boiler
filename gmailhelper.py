import smtplib
import time
import imaplib
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

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
        print str(e)

def get_subject_from_mail(full_email):
    for response_part in full_email:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            email_subject = msg['subject']
            return email_subject

def send_gmail(subject,body):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.FROM_EMAIL
        msg['To'] = config.TO_EMAIL
        msg['Subject'] = subject
        body = body
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(config.SMTP_SERVER,config.SMTP_PORT)
        server.starttls()
        server.login(config.FROM_EMAIL, config.FROM_PWD)
        text = msg.as_string()
        server.sendmail(config.FROM_EMAIL, config.TO_EMAIL, text)
        server.quit()
    except Exception, e:
        print str(e)

def main():
    last_mail = get_last_gmail_from_label(config.LABEL_TO_READ)
    send_gmail(str(float(get_subject_from_mail(last_mail))+0.2),'currenttemp')

if __name__ == "__main__":
    main()
