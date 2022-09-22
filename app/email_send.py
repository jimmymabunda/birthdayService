import smtplib
from decouple import config


#check the .env and set the credentials according
GMAIL_USER = config('GMAIL_USER', cast=str)
PASSWORD = config('PASSWORD')
EMAIL = config('EMAIL')

def sendMessage(names):

    print(names)
    gmail_user = GMAIL_USER
    gmail_password = PASSWORD

    sent_from = gmail_user
    to = [EMAIL]
    subject = 'birthday wishes'
    body = f'Happy Birthday {names}'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)