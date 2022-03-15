from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

import sys

## install: sudo apt install python3-pyvirtualdisplay
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(1680,1050))
#display.start()

def to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

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
user_field.send_keys('usrname')
pass_field = driver.find_element_by_id('password')
pass_field.send_keys('passwd!')
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
