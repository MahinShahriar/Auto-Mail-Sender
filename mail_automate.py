import csv
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

"""
Must Edit below lines ,
line no 
18        email_sender = "sender_example@gmail.com"
19        password = "asdf sdfd sdfs sdfd"
27        attachment_file_paths = ['example.png']

"""

email_sender = "sender_example@gmail.com"
password = "Your_app_password"  #Enter the app password which is generated in gmail(email_sender) account.
subject = "An automated message by pyscript"
body = """
Hello Mahin Al Shahriar.. 
My name is robot.em generated by a pyscript which you wrote a few moments ago.. keep it up. You'll succeed. 
Focus on the main path, and hang with it... Best of Luck !!
"""
# Adding attachments
attachment_file_paths = ['download.png']  # Add your attachment file paths here


# Reading email addresses from CSV file
with open('recipients.csv', 'r') as file:
    reader = csv.reader(file)
    email_recipients = [row[0] for row in reader]


for email_recipient in email_recipients:
    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_recipient
    em['Subject'] = subject
    em.attach(MIMEText(body, 'plain'))

    # Attach files
    for attachment_file_path in attachment_file_paths:
        with open(attachment_file_path, 'rb') as attachment_file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(attachment_file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={attachment_file_path}')
            em.attach(attachment)

    # Sending the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_recipient, em.as_string())
