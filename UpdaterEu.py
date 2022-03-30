import os
import platform
import datetime
from datetime import date
import smtplib
import sys
import getpass




def dater():
		global date2
		if platform.system() == 'Windows':
			if os.path.isfile('C:\\Users\\%username%\\Appdata\\Roaming\\date.data') == False:
				fp = open('C:\\Users\\%username%\\Appdata\\Roaming\\date.data', 'a+')
				daten = str(date.today())
				fp.write(daten)
				fp.close
				os.system("""REG ADD 'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run' /V "EudoxusAPI" /t REG_SZ /F /D "C:\\Users\\%username%\\Appdata\\Roaming\\EudoxusAPI\\UpdaterEu.exe" """)
			else:
				fp = open('C:\\Users\\%username%\\Appdata\\Roaming\\date.data', 'w+')
				daten = str(date.today())
				date2 = fp.read()
				if date2 != daten:
					fp.write(daten)
				else:
					pass

				fp.close()


		if platform.system() == 'Linux':
			global sysuname 
			sysuname = getpass.getuser()
			if os.path.isfile(f'/home/{sysuname}/.EudoxusAPI/date.data') == False:
				with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'a+') as fp1:
					daten = str(date.today())
					fp1.write(daten)
					fp1.close
				with open('/tmp/crontab.X7NVZM/crontab', 'a+') as fp:
					print('@reboot $home.EudoxusAPI/UpdaterEu.py')
			else:
				fp = open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'w+')
				daten = str(date.today())
				date2 = fp.read()
				if date2 != daten:
					fp.write(daten)
				else:
					pass

				fp.close()


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
