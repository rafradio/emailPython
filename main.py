import sys, os
import asyncio
from jinja2 import Environment, FileSystemLoader, Template
import dns.resolver
import socket
from pathlib import Path
import smtplib, ssl
from email_validator import validate_email, EmailNotValidError
from aiosmtpd.controller import Controller
from email.message import EmailMessage
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# class CustomHandler:
#     async def handle_DATA(self, server, session, envelope):
#         peer = session.peer
#         mail_from = envelope.mail_from.append("abdyushev.r@romir.ru")
#         rcpt_tos = envelope.rcpt_tos.append("rafaelab@mail.ru")
#         data = envelope.content         # type: bytes
        
        # Process message data...
        # if error_occurred:
        #     return '500 Could not process your message'
        # return '250 OK'
        
async def templateSendOutlook(args):
    with open("index2.html", "r", encoding="utf-8") as file:
        template_str = file.read()
        
    email_data = {'name': 'Светлана'}
    jinja_template = Template(template_str)
    email_content = jinja_template.render(email_data)
    
    smtp_server = "smtp.lancloud.ru"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls() 
    email = "abdyushev.r@romir.ru"
    data = os.getenv('PASSWORD_OUTLOOK')
    server.login(email, data)
    from_email = email
    to_email = "rafaelab@mail.ru"
    # to_email = "abdyushev.r@romir.ru"
    
    message = MIMEMultipart()
    message['From'] = 'abdyushev.r@romir.ru'
    message['To'] = 'rafaelab@mail.ru'
    message['Subject'] = 'из аутлука'
    message.attach(MIMEText(email_content, "html", 'utf-8'))
    try:
        server.sendmail(from_email, to_email, message.as_string().encode('ascii'))
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused) as e:
        print(e)
    server.quit()

async def sendOutlook(args):
    smtp_server = "smtp.lancloud.ru"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls() 
    email = "abdyushev.r@romir.ru"
    data = os.getenv('PASSWORD_OUTLOOK')
    server.login(email, data)
    from_email = email
    to_email = "rafaelab@mail.ru"
    
    title = 'Почтовая служба'
    msg_content = r"<style>h2{color: blue}</style>"
    msg_content += '<h2>{title}</h2>'.format(title=title)
    msg_content += '<h4>Ваш код - 7893</h4>'
    # msg_content = jinja_template
    # message = MIMEMultipart()
    # message.attach(MIMEText(msg_content, "html"))
    message = MIMEText(msg_content, 'html')
    message['From'] = 'abdyushev.r@romir.ru'
    message['To'] = 'rafaelab@mail.ru'
    message['Subject'] = 'from outlook'
    msg_full = message.as_string()
    # message = "<h2>hello world</h2>"
    # server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{msg_full}")
    try:
        server.sendmail(from_email, to_email, msg_full)
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused) as e:
        print(e)
    server.quit()

    # subject = "from outlook"
    # message = "hello world"
    # res = server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")
    # print(res)
    # server.quit()

async def sendLyb(args):
    smtp_server = "smtp.gmail.com"
    port = 587  # используйте порт 465 для SSL
    server = smtplib.SMTP(smtp_server, port)
    server.starttls() 
    email = "rafradio@gmail.com"
    data = os.getenv('PASSWORD')
    server.login(email, data)
    from_email = email
    to_email = "rafaelab@mail.ru"
    
    # subject = "test"
    title = 'Добрый день'
    msg_content = '<h2>{title}</h2>'.format(title=title)
    msg_content += '<h4>Ваш код - 7893</h4>'
    message = MIMEText(msg_content, 'html')
    message['From'] = 'rafradio@gmail.com'
    message['To'] = 'rafaelab@mail.ru'
    message['Subject'] = 'Any subject'
    msg_full = message.as_string()
    # message = "<h2>hello world</h2>"
    # server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{msg_full}")
    try:
        server.sendmail(from_email, to_email, msg_full)
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused) as e:
        print(e)
    server.quit()

    
        

def optionMain(args):
    records = []
    my_resolver = dns.resolver.Resolver()
    # answers = my_resolver.resolve(host, "A")
    # answer_txt = my_resolver.resolve('megamanager24.ru', "MX")
    answer_txt = my_resolver.resolve('abduyshev.ru', "MX")
    records.extend([str(answer) for answer in answer_txt])
    print(records)
    mxRecord = records[0]
    mxRecord = str(mxRecord)
    host = socket.gethostname()
    # print(host)
    # smtp_server = "smtp.gmail.com"
    # context = ssl.create_default_context()
    # server = smtplib.SMTP()
    # server.set_debuglevel(0)
    # server.connect(smtp_server)
    # server.ehlo() 
    # server.starttls(context=context)
    # server.helo(host)
    # server.mail('rafaelab@mail.ru')
    # code, message = server.rcpt(str("rafradio@gmail.com"))
    # server.quit()
    
    # if code == 250:
    #     print('Success')
    # else:
    #     print('Bad', message)

    # server.mail('rafaelab@mail.ru')
    # code, message = server.rcpt(str('rafaelab@mail.ru'))
    # server.quit()
    # if code == 250:
    #   print('Success')
    # else:
    #     print('Bad')
    
async def srartAsync(args):
    tasks = []
    # task = asyncio.ensure_future(sendLyb(args))
    # task = asyncio.ensure_future(sendOutlook(args))
    task = asyncio.ensure_future(templateSendOutlook(args))
    tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    load_dotenv()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # loop = asyncio.get_event_loop()
    loop.run_until_complete(srartAsync(sys.argv))
    print('hello world')
    # sendOutlook(sys.argv)
    # optionMain(sys.argv)