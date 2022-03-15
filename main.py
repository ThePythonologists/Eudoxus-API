from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

import sys

## install: sudo apt install python3-pyvirtualdisplay
#display = Display(visible=0, size=(1680,1050))
#display.start()

driver = webdriver.Firefox()

url = 'https://eudoxus.gr/'
driver.get(url)

#sleep(.1)
wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
driver.find_element_by_link_text('Έλεγχος Εισόδου Φοιτητή').click()

#sleep(.1)
wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
driver.find_element_by_link_text('εδώ').click()

#sleep(.1)
wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
try:
    driver.find_element_by_link_text('Ελληνικά').click()
except:
    pass

#sleep(.1)
wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
# select = wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user_idp")))
# Select(select).select_by_visible_text("Ιόνιο Πανεπιστήμιο")

arrow = driver.find_elements_by_class_name('select2-selection__arrow')
arrow[0].click()
#sys.exit()

#sleep(.1)
wait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

li = driver.find_elements_by_tag_name('li')
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
user_field = driver.find_element_by_id('username')
user_field.send_keys('inf2021098')
pass_field = driver.find_element_by_id('password')
pass_field.send_keys('Mairaki2003!')
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
td = driver.find_elements_by_tag_name('td')[1:-4]
out = {}
for i,n in enumerate(td):
    if i % 2 == 0:
        key = n.text
    else:
        out[key] = n.text
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
