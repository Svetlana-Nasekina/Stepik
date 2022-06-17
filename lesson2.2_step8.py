import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = ' http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
name.send_keys('Cveta')

fname = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
fname.send_keys('Nas')

emile = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
emile.send_keys('test01102021@yandex.ru')

current_dir = os.path.abspath(os.path.dirname('__file__')) # получаем путь к директории текущего исполняемого скрипта
file_path = os.path.join(current_dir, '4 mb.txt')          # получаем путь к 4 mb.txt
element = browser.find_element(By.XPATH, '/html/body/div/form/input') # ищем кнопку "Загрузить".
element.send_keys(file_path)                               # отправляем файл

browser.find_element(By.XPATH, '/html/body/div/form/button').click()

