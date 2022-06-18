import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
   return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

confirm = browser.switch_to.alert   # в алерте соглашаемся
confirm.accept()

x_element = browser.find_element(By.XPATH, '/html/body/form/div/div/div/label/span[2]')
x = x_element.text
y = calc(x)

fg = browser.find_element(By.XPATH, '/html/body/form/div/div/div/input')
fg.send_keys(y)

browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
