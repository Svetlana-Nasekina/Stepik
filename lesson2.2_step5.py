import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://SunInJuly.github.io/execute_script.html'
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

browser.execute_script("window.scrollBy(0, 150);")   #проскроллить страницу на 150 пикселей

browser.find_element(By.XPATH, '/html/body/div/form/div[2]/input').click()
browser.find_element(By.XPATH, '/html/body/div/form/div[4]/input').click()
browser.find_element(By.XPATH, '/html/body/div/form/button').click()