import sys, os
import dns.resolver
import socket
from pathlib import Path
import smtplib, ssl
from email_validator import validate_email, EmailNotValidError
import yagmail
from email.message import EmailMessage
from dotenv import load_dotenv

def sendLyb(args):
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls() 
    email = "rafradio@gmail.com"
    data = os.getenv('PASSWORD')
    server.login(email, data)
    from_email = email
    to_email = "rafaelab@mail.ru"
    subject = "test"
    message = "test"
    server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")
    server.quit()

    
        

def main(args):
    records = []
    my_resolver = dns.resolver.Resolver()
    # answers = my_resolver.resolve(host, "A")
    answer_txt = my_resolver.resolve('gmail.com', "MX")
    records.extend([str(answer) for answer in answer_txt])
    print(records)
    mxRecord = records[0]
    mxRecord = str(mxRecord)
    host = socket.gethostname()
    print(host)
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    server = smtplib.SMTP()
    server.set_debuglevel(0)
    server.connect(smtp_server)
    server.ehlo() 
    server.starttls(context=context)
    server.helo(host)
    server.mail('rafaelab@mail.ru')
    code, message = server.rcpt(str("rafradio@gmail.com"))
    server.quit()
    
    if code == 250:
        print('Success')
    else:
        print('Bad', message)

    # server.mail('rafaelab@mail.ru')
    # code, message = server.rcpt(str('rafaelab@mail.ru'))
    # server.quit()
    # if code == 250:
    #   print('Success')
    # else:
    #     print('Bad')


if __name__ == "__main__":
    load_dotenv()
    sendLyb(sys.argv)