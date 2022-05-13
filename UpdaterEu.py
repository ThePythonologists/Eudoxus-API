import os
import platform
import datetime
from datetime import date
import smtplib
import sys
import getpass




def dater():
		global sysuname
		sysuname = getpass.getuser()
		global date2
		if platform.system() == 'Windows':
			if os.path.isfile(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data') == False:
				daten = str(date.today())
				with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data', 'a+') as fp:
					fp.write(daten)
				os.system("""REG ADD 'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run' /V "EudoxusAPI" /t REG_SZ /F /D "C:\\Users\\%username%\\Appdata\\Roaming\\EudoxusAPI\\UpdaterEu.exe" """)
			else:
				daten = str(date.today())
				with open('C:\\Users\\%username%\\Appdata\\Roaming\\date.data', 'w+') as fp:
					date2 = fp.read()
					if date2 != daten:
						fp.write(daten)
					else:
						pass

		if platform.system() == 'Linux':
			if os.path.isfile(f'/home/{sysuname}/.EudoxusAPI/date.data') == False:
				daten = str(date.today())
				with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'a+') as fp1:
					fp1.write(daten)
				with open('/tmp/crontab.X7NVZM/crontab', 'a+') as fp:
					print('@reboot $home.EudoxusAPI/UpdaterEu.py')
			else:
				daten = str(date.today())
				with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'w+') as fp:
					date2 = fp.read()
					if date2 != daten:
						fp.write(daten)
					else:
						pass


def email1():
		ouremail='EudoxusAPI@outlook.com'
		receiver= email 
		password='' 
		smtp_server=smtplib.SMTP("smtp.office365.com",587)
		smtp_server.ehlo() 
		smtp_server.starttls() 
		smtp_server.ehlo() 
		smtp_server.login(ouremail,password)

		msg_to_be_sent =(f'''
		This is Eudoxus API and we inform you that 
		you have {days} to take your books! 
		Also those books are available for pick up in the moment: {books}''')

		smtp_server.sendmail(ouremail,receiver,msg_to_be_sent)
		smtp_server.quit()

email = (sys.argv[1])
books = (sys.argv[2])
days  = (sys.argv[3])
dater()
if date2 != date.today():
	email1()
else:
	dater()
