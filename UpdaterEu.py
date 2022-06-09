import os
import platform
import datetime
from datetime import date
import smtplib
import sys
import getpass



sysuname = getpass.getuser() # getting the username
def dater():#here we check if a day has passed or not and if it has we save it for later
		global date2
		if platform.system() == 'Windows':#check for windows
			if os.path.isfile(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data') == False:
				with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data', 'a+') as fp:
					daten = str(date.today())
					fp.write(daten)
				os.system(f"""REG ADD "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /V "EudoxusAPI" /t REG_SZ /F /D "C:\\Users\\{sysuname}\\Appdata\\Roaming\\EudoxusAPI\\UpdaterEu.exe" """)
			else:
				with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data', 'w+') as fp:
					daten = str(date.today())
					date2 = fp.read()
					if date2 != daten:
						fp.write(daten)
					else:
						pass



		if platform.system() == 'Linux':# check for linux 
			if os.path.isfile(f'/home/{sysuname}/.EudoxusAPI/date.data') == False:
				with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'a+') as fp1:
					daten = str(date.today())
					fp1.write(daten)
					fp1.close
				with open(f'/home/{sysuname}/.profile', 'a+') as fp:
					print('python3 $home.EudoxusAPI/UpdaterEu.py')
			else:
				with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'w+') as fp:
					daten = str(date.today())
					date2 = fp.read()
					if date2 != daten:
						fp.write(daten)
					else:
						pass
#some part where is broken by eudoxus the site ;(
"""
def days_downer():
		if platform.system() == 'Windows': 
			with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\days.data', 'a+') as fp:
				days = fp.read()
				dayss = int(days) -1
		if platform.system() == 'Linux':
			with open(f'/home/{sysuname}/.EudoxusAPI/days.data', 'a+') as fp1:
				days = fp.read()
				dayss = int(days) -1
"""

def save_email():#saving the email to a file so we can restart the script normally
	if platform.system() == 'Windows':
		with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\credits2.data', 'a+') as fp:
			fp.write(email)
	if platform.system() == 'Linux':
		with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'a+') as fp1:
			fp1.write(email)

#some part where is broken by eudoxus the site ;(
"""
def save_days():
	if platform.system() == 'Windows':
		with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\days.data', 'a+') as fp:
			fp.write(days)
	if platform.system() == 'Linux':
		with open(f'/home/{sysuname}/.EudoxusAPI/days.data', 'a+') as fp1:
			fp1.write(days)
"""
#here we send an email
def email1():
		global date2
		try:
			ouremail=''
			receiver= email
			password=""
			smtp_server=smtplib.SMTP("smtp.office365.com",587)
			smtp_server.ehlo()
			smtp_server.starttls()
			smtp_server.ehlo()
			smtp_server.login(ouremail,password)
			now = date.today()
			msg_to_be_sent =(f"This is Eudoxus API and we inform that from {date2} and {now} is been 1 day and you have to take your books!!!")
			smtp_server.sendmail(ouremail,receiver,msg_to_be_sent)
			smtp_server.quit()
		except Exception as errorcode:
			print("Failed to send the email error code is : ", errorcode)# in a case where the user doesn't have internet or not. This is only for the developer
			email1()

daten = date.today()
#here is the main we put it on try and except so the script can run without sys.argv[] and more
try:
	email = (sys.argv[1])
	save_email()
	dater()
	if date2 != date.today():
		email1()
		dater()
	else:
		dater()
except: # here we get from the saved data and checks if a day has passed or not and if it does we send an email from here
	if platform.system() == 'Windows': # reading the email from saved data
		with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\credits2.data', 'a+') as fp:
			email = fp.read()
		with open(f'C:\\Users\\{sysuname}\\Appdata\\Roaming\\date.data', 'w+') as fp:
			date2 = fp.read()
	if platform.system() == 'Linux':
		with open(f'/home/{sysuname}/.EudoxusAPI/credits2.data', 'a+') as fp1:
			email = fp1.read()
		with open(f'/home/{sysuname}/.EudoxusAPI/date.data', 'a+') as fp1:
			date2 = fp1.read()
	if date2 !=  daten:
		email1()
		dater()
	else:
		dater()
