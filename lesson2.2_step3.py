import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

a_el = browser.find_element(By.XPATH, '/html/body/div/form/h2/span[2]')
a = a_el.text
b_el = browser.find_element(By.XPATH, '/html/body/div/form/h2/span[4]')
b = b_el.text
x2 = (int(a)+int(b))  #сложили два числа

fg = browser.find_element(By.XPATH, '/html/body/div/form/div/select')
fg.send_keys(x2)     #выбрали сумму чисел в выпадашке

browser.find_element(By.XPATH, '/html/body/div/form/button').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
