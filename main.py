import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "[CHANGEME]"
recevier_email = "[CHANGEME]"

message = MIMEMultipart("")
message["Subject"] = "[CHANGEME]"
message["From"] = sender_email
message["To"] = recevier_email

text = """\
Message
"""

part1 = MIMEText(text, "plain")
message.attach(part1)

filepath = "[CHANGEME]"
part2 = MIMEBase('application', "octet-stream")
part2.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part2)

part2.add_header('Content-Dispasition', 'attachment; filename="[CHANGEME]"')

message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP("mail.securelawfrim.com",587)
server.starttls()
server.ehlo_or_helo_if_needed()
server.sendmail(
    sender_email, recevier_email, message.as_string()
)
