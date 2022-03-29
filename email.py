import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)


message = MIMEMultipart()


message['From'] = MY_ADDRESS
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Απόθεμα Συγγραμμάτων"


textPart = MIMEText("Ενημέρωση", '...')

message.attach(textPart)

server.send_message(message)
server.quit()