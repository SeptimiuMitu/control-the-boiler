import smtplib
import time
import imaplib
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "johndoe" + ORG_EMAIL
FROM_PWD    = "password"
TO_EMAIL    = "johndoe" + ORG_EMAIL
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT   = 993
LABEL_TO_READ = 'currenttemp'

def get_last_gmail_from_label(gmail_label):
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
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
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, FROM_PWD)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, TO_EMAIL, text)
    server.quit()

def main():
    last_mail = get_last_gmail_from_label(LABEL_TO_READ)
    send_gmail(str(float(get_subject_from_mail(last_mail))+0.2),'currenttemp')

if __name__ == "__main__":
    main()
