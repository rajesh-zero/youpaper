"""python py file to handle mails stuffs """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

YOUPAPER_EMAIL = ""
YOUPAPER_PASSWORD = ""

SENDER = ""


def make_and_mail(receiver, subject, body):
    """
    Creates and sends email to receiver.
    """
    emailbody = MIMEText(body, 'html')
    msg = MIMEMultipart('alternative')
    msg['From'] = SENDER
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(emailbody)
    #pylint: disable=invalid-name
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(YOUPAPER_EMAIL, YOUPAPER_PASSWORD)
        s.sendmail(SENDER, receiver, msg.as_string())
        s.quit()
        return 1 #returns 1 if success
    except smtplib.SMTPException:
        return 0 #returns 0 if failure
