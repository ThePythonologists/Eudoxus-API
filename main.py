from inspect import _void
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys

from time import sleep
driver = webdriver.Firefox()

url = 'https://sso.ionio.gr/login?service=https%3A%2F%2Fidp.ionio.gr%2Fcasauth%2Ffacade%2Fnorenew%3Fidp%3Dhttps%3A%2F%2Fidp.ionio.gr%2Fidp%2FexternalAuthnCallback.html'
url = 'https://eudoxus.gr/'
driver.get(url)

sleep(.5)
driver.find_element_by_link_text('Έλεγχος Εισόδου Φοιτητή').click()

sleep(.5)
driver.find_element_by_link_text('εδώ').click()

sleep(.5)
select(select).select_by_visible_text("Ionian University")
#select(select).select_by_visible_text("Ιόνιο Πανεπιστήμιο")
#select se = new Select(driver.findElement(By.xpath("//*[@id=/"select2-user_idp-mf-result-77w3-https://idp.ionio.gr/idp/shibboleth"]']")));
#set.selectByIndex(12)


arrow = driver.find_elements_by_class_name('select2-selection__arrow')
print(type(arrow[0]))
for n in arrow:
    print(n)
arrow[0].click()
#sys.exit()

sleep(.5)

select = Select(driver.find_element_by_name("user_idp"))
#wait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "user_idp")))

#driver.find_element_by_name("user_idp").click()
sleep(.5)
select.select_by_index(2)


