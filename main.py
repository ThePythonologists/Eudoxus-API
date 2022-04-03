from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import tkinter
import os
#from Crypto.Cipher import AES
import platform
from tkinter import *
import requests
from PIL import Image, ImageTk
import sys

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

def get_history_table_and_buttons(driver):
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

   
def Main():

    driver = webdriver.Firefox()

    url = 'https://eudoxus.gr/'
    driver.get(url)

    #sleep(.1)
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
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
            driver.find_element_by_link_text('εδώ').click()
        except:
            pass
            #print('except 2')
        finally:
            #print('finally 2')
            break
    while True:
        try:
            driver.find_element_by_link_text('Ελληνικά').click()
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
            arrow = driver.find_elements_by_class_name('select2-selection__arrow')
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
            li = driver.find_elements_by_tag_name('li')
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
    wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
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

def exit():
    sys.exit()
#some fuctions we will use in the future later
def bookstatus():
    return

def buttonpress(): # this "buttonpress" actually starts/triggers/calls the program UpdaterEu 
    if platform.system() == 'Windows': # of course we check to see if the platform is windows or linux
        os.system('C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI\\UpdaterEu.exe {email} {books} {day}')
    if platform.system() == 'Linux': # Cause "A linux computer is like air conditioning - it becomes useless when you open Windows. " — Linus T.
        os.system('python3 $home.EudoxusAPI/UpdaterEu.py ')

def updates(): # here we create another window thats going to ask the user for there email so we can send them live updates about there books
    Updateswindow = Toplevel(root)
    Updateswindow.geometry("400x100")
    Updateswindow.resizable(0, 0)
    Updateswindow.title("Give us your email to send you updates")
    text = Entry(Updateswindow, width= 30)
    text.pack()
    Button(Updateswindow, text="Done", command=buttonpress).pack()# this part is where we start another program (UpdaterEu.py)
    

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


if(platform.system() == 'Windows'): #here we download eudoxus image from the main url of eudoxus plus we create a directory where we save some data for later use
    os.system("mkdir C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI")
    bla = "%username%"
    os.system(f'curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o C:\\Users\\{bla}\\AppData\\Roaming\\EudoxusAPI\\logo.png')

if platform.system() == 'Linux':
    try:
        os.system('mkdir $home.EudoxusAPI && cd $home.EudoxusAPI')
        os.system('curl -L https://service.eudoxus.gr/images/eudoxus-logo.png -o logo.png' )
    except:
        if os.system('whoami') == 'root\n0':
            os.system('cd /root/.EudoxusAPI')
        pass
# some basic parameteres for the root window or GUI window like how big is going to be, title of the window and not allowing to the user change size of the window cause its going to break the style of it.
root = Tk()
root.geometry("500x500")
root.wm_title('EudoxusAPI')
root.resizable(0, 0)
if platform.system() == 'Linux': #adding eudoxus image here and checking if it is windows or linux the platform that is running
    img = ImageTk.PhotoImage(Image.open("logo.png"))


if platform.system() == 'Windows':
    os.system('cd C:\\Users\\%username%\\AppData\\Roaming\\EudoxusAPI')
    bla = "%username%"
    img = ImageTk.PhotoImage(Image.open("logo.png"))

image = Label(root, image = img)

#adding/configuring some buttons here
button = Button(root, text="Login to Eudoxus", command = Main)
button1 = Button(root, text="Exit", command = exit)
button2 = Button(root, text="Book status", command = bookstatus)
button3 = Button(root, text="Give me live-updates", command =updates)

# placing my buttons on the GUI app
image.place(x = 70, y = 70)
button.place(x=285, y=450)
button1.place(x=425, y=450)
button2.place(x=180, y=450)
button3.place(x=10, y = 450)
#here we create a menu where we added an "About" options for viewing licenses and exit (this menu will become usefull in the futere)
menubar = Menu(root)
root.config(menu=menubar)
about = Menu(menubar)
menubar.add_cascade(label='About', menu = about)
about.add_command(label="Licenses", command = Licenses)
about.add_separator()
about.add_command(label="Exit", command = exit)


root.mainloop()
