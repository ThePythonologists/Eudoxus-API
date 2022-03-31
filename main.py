import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
server.login('thepythonologists@gmail.com', 'mairaki2003')


message = MIMEMultipart()


message['From'] = 'thepythonologists@gmail.com'
message['To'] = 'giann.pavlos@gmail.com'
message['Subject'] = "Απόθεμα Συγγραμμάτων"


textPart = MIMEText("Χαίρεται φοιτητή/φοιτή,\n Σου αποστέλλουμε τα δεδομένα που συλλέξαμε από την βάση δεδομένων του Ευδόξου για την άμεση ενημέρωση σου σχετικά με τα παρακάτω συγγράμματα:", 'plain')

message.attach(textPart)

server.send_message(message)
server.quit()
