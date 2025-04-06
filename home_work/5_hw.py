from selenium import webdriver
from selenium.webdriver.common.by import By


def find_element():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    field_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    field_password = driver.find_element(By.CSS_SELECTOR, '#password')
    button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if field_username and field_password and button_submit is None:
        print('Элементы не найдены')
    else:
       print('Элементы найдены')
find_element()