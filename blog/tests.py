import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys("gdega")
    driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys("Filipek123")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="user-tools"]/a[1]').click()
    driver.find_element(By.XPATH,'/html/body/nav/div/a/span').click()

element_is_clickable()

def respons_check(w,file):
    height=768
    driver.set_window_size(w,height)
    driver.save_screenshot(file)

respons_check(900,"test900.png")
respons_check(1200,"test1200.png")
respons_check(1800,"test1800.png")
respons_check(600,"test600.png")