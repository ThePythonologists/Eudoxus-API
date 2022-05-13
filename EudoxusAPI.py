from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import messagebox
import tkinter
import os, getpass
import platform
from tkinter import *
import requests
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import sys

whoami = getpass.getuser()
checkos = platform.system()

## install: sudo apt install python3-pyvirtualdisplay
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(1680,1050))
#display.start()

##########################################
#### The Creation of our Dictionary   ####
#### which keeps the information that ####
#### our program will use later       ####
##########################################

def to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

################################################
#### The def "get history_table_and_buttons ####
#### is required for the selenium driver    ####
#### in order to proceed to the next urls   ####
################################################

def get_history_table_and_buttons(driver):                                              #This specific function called get_history_table_and_buttons(driver) reads the history table and returns a list with things such as buttons. The fuction searches through lists, arrays and tds in html format to find the  element button in order to save it for the selenium driver.
    ''' reads the history table and returns a list of lists                             
        Each inner list contains:
                Ημερομηνία - text
                Έτος       - text
                Περίοδος   - text
                Button     - text
                Button     - clickable element
    '''
    out = []
    the_table = None
    tables = driver.find_elements_by_tag_name('table')
    for a_table in tables:
        thead = a_table.find_element_by_tag_name('thead')
        if 'Ημερομηνία' in thead.text:
            the_table = a_table
            #print('table found!!!')
            break
    if the_table:
        tbody = the_table.find_element_by_tag_name('tbody')
        tr = tbody.find_elements_by_tag_name('tr')
        for a_tr in tr:
            new_td = []
            td = a_tr.find_elements_by_tag_name('td')
            for a_td in td:
                #print(a_td.text)
                new_td.append(a_td.text)
                if 'Ενημέρωση' in a_td.text or \
                        'Επισκόπηση' in a_td.text:
                    #print('  button ')
                    button = a_td.find_element_by_tag_name('button')
                    new_td.append(button)
                    #button.click()
                    #print('  button clicked ')
            out.append(new_td)
    return out

def continue_driver(driver):                                                          #This function does the same thing as the history and buttons function.
    ''' reads the available lists and returns them
        The specific one contains:
               Button - text (Συνέχεια)
               Button - clickable element
    '''
    out = []
    the_table = None
    tables = driver.find_elements_by_tag_name('table')
    for a_table in tables:
        thead = a_table.find_element_by_tag_name('thead')
        if 'Τροποποίηση Δήλωσης' in thead.text:
            the_table = a_table
            #print('table found!!!')
            break
    if the_table:
        tbody = the_table.find_element_by_tag_name('tbody')
        tr = tbody.find_elements_by_tag_name('tr')
        for a_tr in tr:
            new_td = []
            td = a_tr.find_elements_by_tag_name('td')
            for a_td in td:
                #print(a_td.text)
                new_td.append(a_td.text)
                if 'Τροποποίηση Εξαργύρωσης' in a_td.text or \
                        'Συνέχεια' in a_td.text:
                    #print('  button ')
                    button = a_td.find_element_by_tag_name('button')
                    new_td.append(button)
                    #button.click()
                    #print('  button clicked ')
            out.append(new_td)
    return out


def Main():                                              #This function is using the selenium driver in order to track the urls and click them for the user.

    driver = webdriver.Firefox()

    url = 'https://eudoxus.gr/'
    driver.get(url)

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')     #using the sleep mode in selenium we give some time for the driver to search the buttons and afterwards will click them.
    while True:
        try:
            driver.find_element_by_link_text('Έλεγχος Εισόδου Φοιτητή').click()
        except:
            pass
            #print('except 1')
        finally:
            #print('finally 1')
            break

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    while True:
        try:
            driver.find_element_by_link_text('εδώ').click()   #the driver clicks the button "εδώ" in the eudoxus site.
        except:
            pass
            #print('except 2')
        finally:
            #print('finally 2')
            break
    while True:
        try:
            driver.find_element_by_link_text('Ελληνικά').click()        #the driver changes the language from english to greek
        except:
            pass
            #print('except 3')
        finally:
            #print('finally 3')
            break

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    # select = wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user_idp")))
    # Select(select).select_by_visible_text("Ιόνιο Πανεπιστήμιο")

    while True:
        try:
            arrow = driver.find_elements_by_class_name('select2-selection__arrow')   #The driver is looking for an element by a specific class name in order to click it from the drop-down menu
        except:
            pass
            #print('except 4')
        finally:
            #print('finally 4')
            if arrow:
                break
    arrow[0].click()
    #sys.exit()

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    while True:
        try:
            li = driver.find_elements_by_tag_name('li')    #If the drivers find the value of the class then proceeds to the next page
        except:
            pass
            #print('except 5')
        finally:
            #print('finally 5')
            if li:
                break
    for n in li:
        #print(n.text + '\n')
        if n.text == 'Ιόνιο Πανεπιστήμιο':
            n.click()
            break

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    buttons = driver.find_elements_by_tag_name('button')
    if len(buttons) == 1:
        buttons[0].click()
    else:
        for n in buttons:
            if n.text == 'Επιβεβαίωση':
                n.click()
                break

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')   #Here, the frontend passes the keys (username & password) from the user and fills it in the specific form which uses Shibboleth.sso from the selected university.
    #driver.refresh()
    while True:
        try:
            user_field = driver.find_element_by_id('username')
        except:
            pass
            #print('except 6')
        finally:
            #print('finally 6')
            if user_field:
                break
    user_field.send_keys('')
    pass_field = driver.find_element_by_id('password')
    pass_field.send_keys('')
    buttons = driver.find_elements_by_id('submitForm')[0].click()


    wait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'td')))
    td = driver.find_elements_by_tag_name('td')[:10]
    out = {}
    for i,n in enumerate(td):
        if i % 2 == 0:
            key = n.text
        else:
            out[key] = n.text
    print(out)
    print('\n')
    for n in out.keys():
        print('{0} {1}'.format(n, out[n]))
    print('\n')

    l = driver.find_elements_by_tag_name('a')
    #help(l[0])
    for n in l:
        if 'υποβολής' in n.text:
            n.click()
            break

    sleep(3)
    #wait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'td')))
    while True:
        try:
            td = driver.find_elements_by_tag_name('td')
        except:
            pass
            #print('except 7')
        finally:
            #print('finally 7')
            if td:
                break
    out = {}
    outl = []
    ind = 0
    for n in td:
        if n.text != '':
            outl.append(n.text)
    out = to_dict(outl[:-4])
    print(out)
    print('\n')
    for n in out.keys():
        print('{0}: {1}'.format(n, out[n]))

    l = driver.find_elements_by_tag_name('a')
    for n in l:
        #print(n.text)
        if 'Δηλώσεις Συγγραμμάτων' in n.text:
            n.click()
            break

    #driver.quit()

    ###################################
    #### Data Extraction and Click ####
    ###################################

    data = get_history_table_and_buttons(driver)

    if data:
        print('\n\n', data)

        # click last Update button
        data[-2][-1].click()

        # click Επισκόπηση
        # data[-1][-1].click()

        # walk list
        print('\n\n')
        for i, d in enumerate(data):
            print('Element', i)
            for n, dd in enumerate(d):
                print('  data', n, ':', dd)

 #driver.quit()
def Decrypt():

    if(platform.system() == 'Windows'):
            os.chdir(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\")
            with open('other.logs', 'rb') as maybekey:
                Halo = maybekey.read()
            fernet = Fernet(Halo)
            with open('credits.log.enc','rb') as encryptfile:
                content = encryptfile.read()
            decrypted = fernet.decrypt(content)
            with open('credits.log', 'wb') as dcontent:
                dcontent.write(decrypted)
            os.system("mv credits.log C:\\Users\\%username%\\AppData\\Roaming\\Temp\\")
    if platform.system() == 'Linux':
            os.chdir(f"/home/{whoami}/.EudoxusAPI/")
            with open('other.logs', 'rb') as maybekey:
                Halo = maybekey.read()
            fernet = Fernet(Halo)
            with open('credits.log.enc','rb') as encryptfile:
                content = encryptfile.read()
            decrypted = fernet.decrypt(content)
            with open('credits.log', 'wb') as dcontent:
                dcontent.write(decrypted)
            os.system('mkdir /tmp/000')
            os.system('mv credits.log /tmp/000/')
def exit():
    sys.exit()
#some fuctions we will use in the future later
def bookstatus():
    return

def buttonpress(): # this "buttonpress" actually starts/triggers/calls the program UpdaterEu
    if checkos == 'Windows': # of course we check to see if the platform is windows or linux
        os.system('C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI\\UpdaterEu.exe {email} {books} {day}')
    if checkos == 'Linux': # Cause "A linux computer is like air conditioning - it becomes useless when you open Windows. " — Linus T.
        os.system('python3 $home.EudoxusAPI/UpdaterEu.py ')

def updates(): # here we create another window thats going to ask the user for there email so we can send them live updates about there books
    Updateswindow = Toplevel(root)
    Updateswindow.geometry("400x100")
    Updateswindow.resizable(0, 0)
    Updateswindow.title("Give us your email to send you updates")
    text = Entry(Updateswindow, width= 30)
    text.pack()
    Button(Updateswindow, text="Done", command=buttonpress).pack()# this part is where we start another program (UpdaterEu.py)

def Encrypt(user,passwd):
    if(checkos == 'Windows'):
        os.chdir(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI")
        with open('credits.log','w') as fp:
            fp.write(user + '\n' + passwd)
        Halo = Fernet.generate_key()
        with open('other.logs', 'wb') as maybekey:
            maybekey.write(Halo)
        with open('other.logs', 'rb') as maybekey:
            maybekey2 = maybekey.read()
        fernet = Fernet(maybekey2)
        with open('credits.log','rb') as creditss :
            content = creditss.read()
        encrypt = fernet.encrypt(content)
        with open('credits.log.enc','wb') as encryptfile:
            encryptfile.write(encrypt)
        os.system("del C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI\\credits.log")

    if checkos == 'Linux':
        os.chdir(f"/home/{whoami}/.EudoxusAPI")
        with open('credits.log','w') as fp:
            fp.write(user + '\n' + passwd)
        Halo = Fernet.generate_key()
        with open('other.logs', 'wb') as maybekey:
            maybekey.write(Halo)
        with open('other.logs', 'rb') as maybekey:
            maybekey2 = maybekey.read()
        fernet = Fernet(maybekey2)
        with open('credits.log','rb') as creditss :
            content = creditss.read()
        encrypt = fernet.encrypt(content)
        with open('credits.log.enc','wb') as encryptfile:
            encryptfile.write(encrypt)

            os.system("rm ~/.EudoxusAPI/credits.log")
    return

def Licenses(): # well when we create the menu we have an option thats called "Licenses" well it does what it says shows you the licenses
    Line_window = Toplevel(root)
    Line_window.title("Licenses")
    Label(Line_window,text ="""MIT License
    Copyright (c) 2022 ThePythonologists
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.""").pack()

def check(user,passw): # checking the anwser
    username1 = len(user.get())
    password1 = len(passw.get())
    username = str(user.get())
    password = str(passw.get())
    print(username, password)
    if username1 == 0 or password1 == 0 :
            question = messagebox.showerror("Error","You didn't gave us your username or password or none of them")
            PreMain()
    else:
        secwind.destroy()
        if checkos == 'Linux':

            os.chdir(f"/home/{whoami}/.EudoxusAPI/")
            if os.path.exists(f"/home/{whoami}/.EudoxusAPI/credits.log.enc") == True :
                Decrypt()
            else:
                Encrypt(username,password)
        if(checkos == 'Windows'):

            os.chdir(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\")
            if os.path.exists(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\credits.log.enc") == True :
                Decrypt()
            else:
                Encrypt(username,password)

        Main()

def PreMain(): # here we are capturing (while we are asking the user) for his password and username if they dont want there credentials to be saved in there disk (and yes they are encrypted) we go to the Main code in which is the def Main()
    global secwind
    global password
    global username
    if question == 1:
        secwind = Toplevel(root)
        secwind.title("Login")
        secwind.geometry("350x100")
        Label(secwind, text = "username").place(x=0, y=1)
        Label(secwind, text = "password").place(x=0, y=25)
        usernamewiget = Entry(secwind, width= 20)
        passwordwiget = Entry(secwind, show="*", width= 20)
        butt0n = Button(secwind, text="Done", command = lambda: check(usernamewiget,passwordwiget))
        usernamewiget.pack()
        passwordwiget.pack()
        butt0n.pack()
    else:
        Main()

def PreMain1():
    global username,password             # We check if the credits.log.enc exists or not so we dont ask the user to enter his credentials
    global question
    question2 = messagebox.showwarning("Attention !","On a moment you will see your browser poping up and doing stuff automatically , dont worry this is just a normal process of this program")
    if checkos == 'Windows' and os.path.exists("C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\credits.log.enc") == True:
        Decrypt()
        os.chdir(f"C:\\Users\\{whoami}\\AppData\\Roaming\\Temp")
        with open("credits.log","rb") as reader:
            username = reader.readline(1)
            password = reader.readline(3)
        Main()
    if checkos == 'Linux' and os.path.exists(f"/home/{whoami}/.EudoxusAPI/credits.log.enc") == True :
        Decrypt()
        os.chdir("/tmp/000")
        with open("credits.log","r") as reader:
            username = reader.readline(1)
            password = reader.readline(3)
        Main()

    question = messagebox.askyesno("QUESTION","Do you want to save your password and username so you don't have to login again?")
    PreMain()

bla = "%username%" #here we download eudoxus image from the main url of eudoxus plus we create a directory where we save some data for later use
if checkos == 'Windows':
        if os.path.exists(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI") == False:
                os.system("mkdir C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI")
                os.system(f'curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o C:\\Users\\{bla}\\AppData\\Roaming\\EudoxusAPI\\logo.png')
        elif os.path.exists(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\logo.png") == False:
                os.system(f'curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o C:\\Users\\{bla}\\AppData\\Roaming\\EudoxusAPI\\logo.png')
        else:
                pass
if checkos == 'Linux' :
        if (os.path.exists(f"/home/{whoami}/.EudoxusAPI/logo.png") == False and os.path.exists(f"/home/{whoami}/.EudoxusAPI") == True):
                os.system(f'cd /home/{whoami}/.EudoxusAPI/ && curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o logo.png' )
        elif os.path.exists(f"/home/{whoami}/.EudoxusAPI") == False:
                os.system('mkdir $home.EudoxusAPI && cd $home.EudoxusAPI')
                os.system(f'cd /home/{whoami}/.EudoxusAPI/ && curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o logo.png' )
        else:
                pass

# some basic parameteres for the root window or GUI window like how big is going to be, title of the window and not allowing to the user change size of the window cause its going to break the style of it.
root = Tk()
root.geometry("500x500")
root.wm_title('EudoxusAPI')
root.resizable(0, 0)
if checkos == 'Linux': #adding eudoxus image here and checking if it is windows or linux the platform that is running
    os.chdir(f"/home/{whoami}/.EudoxusAPI/")
    img = ImageTk.PhotoImage(Image.open("logo.png"))


if checkos == 'Windows':
    os.chdir(f'C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI')
    img = ImageTk.PhotoImage(Image.open("logo.png"))

image = Label(root, image = img)

def Remover():
    if(checkos == 'Windows'):
        os.chdir(f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI")
        if os.path.exists((f"C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\credits.log")) == True:
            os.system(f"del C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\credits.log")
            os.system(f"del C:\\Users\\{whoami}\\AppData\\Roaming\\EudoxusAPI\\other.logs")
        else:
            messagebox.showerror("Error","You are not logged in !")
    if checkos == 'Linux':
        os.chdir(f"/home/{whoami}/.EudoxusAPI/")
        if os.path.exists(f"/home/{whoami}/.EudoxusAPI/credits.log.enc") == True :
            os.system(f"rm /home/{whoami}/.EudoxusAPI/credits.log.enc")
            os.system(f"rm /home/{whoami}/.EudoxusAPI/other.logs")
        else:
            messagebox.showerror("Error","You are not logged in !")

#adding/configuring some buttons here
button = Button(root, text="Login to Eudoxus", command = PreMain1)
button1 = Button(root, text="Exit", command = exit)
button2 = Button(root, text="Book status", command = bookstatus)
button3 = Button(root, text="Give me live-updates", command =updates)

# placing my buttons on the GUI app
image.place(x = 70, y = 70)
button.place(x=285, y=450)
button1.place(x=425, y=450)
button2.place(x=180, y=450)
button3.place(x=10, y = 450)
#here we create a menu where we added an "About" options for viewing licenses and exit (this menu will become usefull in the future)
menubar = Menu(root)
root.config(menu=menubar)
about = Menu(menubar)
menubar.add_cascade(label='Options', menu = about)
about.add_command(label="View Licenses", command = Licenses)
about.add_command(label="Remove saved data", command = Remover)
about.add_command(label="Exit", command = exit)


root.mainloop()
