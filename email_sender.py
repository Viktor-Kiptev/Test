import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_var = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Viktor'
email['to'] = 'viktor-kiptev@hotmail.com'
email['subject'] = 'Some text for subject'

email.set_content(html_var.substitute({'name': 'Viktor'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vk.introduct@gmail.com', '********')
    smtp.sendmail(email)
    print('finished')
