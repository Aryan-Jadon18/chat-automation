from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("please scan qr code and press ay key to continue: ")
RM= driver.find_element_by_css_selector('span[title="Aryan Singh Jadon"]')
RM.click()
testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[19]/div/div/div[2]/div[1]/div[1]/span")
time.sleep(10)
testinput.send_keys("Happy Birthday")
testinput.send_keys(Keys.RETURN)