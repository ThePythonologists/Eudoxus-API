import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
server.login('thepythonologists@gmail.com', 'mairaki2003')


message = MIMEMultipart()


message['From'] = 'thepythonologists@gmail.com'
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Απόθεμα Συγγραμμάτων"


textPart = MIMEText("Ενημέρωση", '...')

server.send_message(message)
server.quit()
