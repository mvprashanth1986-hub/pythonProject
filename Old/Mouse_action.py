from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.spicejet.com/")
driver.maximize_window()

driver.implicitly_wait(10)

action = ActionChains(driver)

ele = driver.find_element(By.ID,'ctl00_HyperLinkLogin')

action.move_to_element(ele).perform()

driver.implicitly_wait(10)
time.sleep(10)

ele = driver.find_element(By.LINK_TEXT,'SpiceClub Members')

driver.implicitly_wait(10)
time.sleep(10)

action.move_to_element(ele).perform()

driver.implicitly_wait(10)
time.sleep(10)

ele = driver.find_element(By.LINK_TEXT,'Member Login')

ele.click()



