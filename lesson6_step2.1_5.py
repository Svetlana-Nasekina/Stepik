from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
   return str(math.log(abs(12 * math.sin(int(x)))))   #Используйте функцию calc(), которая рассчитает и
                                                           # вернет вам значение функции, которое нужно ввести в текстовое поле.


x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)


fg = browser.find_element(By.XPATH, '//*[@id="answer"]')
fg.send_keys(y)
browser.find_element(By.XPATH, '/html/body/div/form/div[2]/label').click()
browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label').click()
browser.find_element(By.XPATH, '/html/body/div/form/button').click()

#time.sleep(10)
# закрываем браузер после всех манипуляций
#browser.quit()