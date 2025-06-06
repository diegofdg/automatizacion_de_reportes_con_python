from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor = 'xxxxxxxx@gmail.com'
email_password = 'xxxx xxxx xxxx xxxx'
email_receptor = 'xxxxxxxx@gmail.com'

asunto = 'Mail desde Python'
cuerpo = 'Te envío un email con una imagen adjunta desde mi script de Python'
em = EmailMessage()
em['FROM'] = email_emisor
em['to'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

with open('project-mail/image.png', 'rb') as file:
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_emisor, email_password)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
