from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.XPATH, '/html/body/div/form/div/div/div[1]/h2/img')
x = x_element.get_attribute('valuex')
y = calc(x)

fg = browser.find_element(By.XPATH, '//*[@id="answer"]')
fg.send_keys(y)

browser.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/input[1]').click()
browser.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/input[3]').click()
browser.find_element(By.XPATH, '/html/body/div/form/div/div/button').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
